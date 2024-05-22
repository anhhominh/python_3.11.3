import hashlib
import re
from uuid import uuid4
import uuid

import pandas as pd

def gen_id():
    return hashlib.md5(str(uuid.uuid1()).encode('utf-8')).hexdigest()

def get_type(url):
    if isinstance(url, str) and is_include_url(url):
        if is_video(url):
            return 'video'
        if is_audio(url):
            return 'audio'
        if is_image(url):
            return 'image'
    else:
        return 'html'

def create_list_series_keo_tha_vao_o_trong(body):
    if body is None or len(body) == 0:
        return None
    content = {
        'type': 'series',
        "style": {
            "display": "list-item"
        },
        'value': [],
        'list_select': []
    }
    answer = {
        'style': 0,
        'answers_list': []
    }
    for item in body:
        if isinstance(item, str):
            # Tạo answer
            tmp0 = re.findall(r"\[([^\]]+)\]", str(item).strip())
            count = sum(1 for i in tmp0 if i == '@')
            print(count)
            print("-----------------")
            if len(tmp0) > 0:
                for i in tmp0:
                    if i != '@':
                        list_value = []
                        split_or = i.split('|')
                        print(split_or)
                        for x in split_or:
                            print(sum(1 for i in x if i == '@'))
                            print(x)
                            if "@" in x and len(x) > 1 and sum(1 for i in x if i == '@') >= 1 : #and split_or.index(x) > 1:
                                # print(x)
                                ans = {
                                    'id': gen_id(),
                                    'correct_value': [x.replace("@", "", 1)]
                                }
                                answer['answers_list'].append(ans)
                                list_value.append(x.replace("@", "", 1))
                                continue
                            if x != '':
                              list_value.append(x)
                        if len(list_value) < count:
                            return
                        item_select = {
                            'id': gen_id(),
                            'list_value': list_value
                        }
                        content['list_select'].append(item_select)
            content['value'].append({
                'type': 'html',
                 'value': re.sub(r'\[(?!@)[^]]*\]', "", str(item).strip())
            })
        elif isinstance(item, int):
            content['value'].append({
                'type': 'html',
                'value': str(item)
            })
        else:
            link = item[0] if len(item) > 0 else None
            if link is not None:
                content['value'].append({
                    'type': get_type(link),
                    'value': item[0]
                })
    print(content)
    print(answer)
    return content, answer

def is_blank(chars: str):
    return not (chars and chars.strip())

def get_content_keo_tha_vao_o_trong(row):
    error = None
    data = None
    answer = None
    try:
        # content = row['content'] if not pd.isna(row['content']) else None
        content = row
        if isinstance(content, str) and not is_blank(str(content)):
            token = re.split(r'<br ?/?>|\\n|\n|\\\\n', content)
            list_content = []
            for item in token:
                # if is_include_url(item):
                #     list_url = get_url(content)
                #     list_content.append(list_url)
                # else:
                    tmp = str(item).strip()
                    if not is_blank(str(tmp)):
                        list_content.append(tmp)

            if len(list_content) >= 1:
                data, answer = create_list_series_keo_tha_vao_o_trong(list_content)
                # print(data)
    except Exception as e:
        error = f"Có lỗi trong quá trình xử lý <content>: {repr(e)}"
    return data, answer, error

def get_text_search_dien_chon_tu_co_san(row):
    error = None
    data = None
    try:
        data = row #row['content'] if not pd.isna(row['content']) else ""
        regex = r'https?://\S+|www\.\S+'
        data = re.sub(regex, '', data)

    except Exception as e:
        error = f"Có lỗi trong quá trình xử lý <text_search>: {repr(e)}"
    # print(data)
    return data, error

def decode_content_keo_tha_vao_o_trong(cau_hoi_dien_chon_tu_co_san):
    data = []
    for i in cau_hoi_dien_chon_tu_co_san:
        if i['content'] and 'type' in i['content'] and 'value' in i['content']:
            content = i['content']
            answer = i['answer']
            answers_list = []
            correct_value = []
            list_select = []
            if answer:
                answers_list = answer["answers_list"]
            if answers_list:
                for answers in answers_list:
                    correct_value.append(answers["correct_value"][0])
            for select in content["list_select"]:
                list_select.append(select["list_value"])
            values = []
            index = 0
            if content["type"] == "series":
                for x in content["value"]:
                    value = x["value"]
                    if "@[@]" in value:
                        count = value.count("@[@]")
                        if len(list_select[index]) >= count:
                                correct_value_string = ''
                                for i in correct_value:
                                    correct_value_string = correct_value_string + f"|@{i}"
                                list_item_select = "|".join(list_select[index])
                                value = value + f"[|{list_item_select}{correct_value_string}|]"
                                index += 1
                    values.append(value)
                value = "\n ".join(values)
                data.append(value)
            else:
                value = content["value"]
                correct_value_string = f"|@{correct_value[index]}"
                list_item_select = "|".join(list_select[index])
                value = value.replace("@[@]", f"[{list_item_select}{correct_value_string}]")
                data.append(value)

        else:
            data.append(None)
    print(data)
    return data

if __name__ == "__main__":
    get_content_keo_tha_vao_o_trong('https://media.trangnguyen.edu.vn/uploads/2019/De%20thi%202023/Do%20vat/minh_la_sach%203x3.png \n Chúng mình là @[@]. Trong tên chúng mình có vần @[@].[|@@|test|quyển sách|@ach|]')
    data = {
  "owner_id": "TRANG_NGUYEN",
  "log_created_user_id": "btthu",
  "log_updated_user_id": "b0f6f55c-c5cf-4f55-9962-5f76d3b73985",
  "log_deleted_user_id": None,
  "log_created_time": {
    "$numberLong": "1714720334923"
  },
  "log_updated_time": {
    "$numberLong": "1714979956691"
  },
  "log_deleted_time": None,
  "log_is_deleted": 0,
  "log_updated_info": None,
  "log_deleted_info": None,
  "log_approved_user_id": "b0f6f55c-c5cf-4f55-9962-5f76d3b73985",
  "log_created_user_name": None,
  "log_approved_user_name": "btthu",
  "log_approved_time": {
    "$numberLong": "1714979956691"
  },
  "lesson_question_id": "6c1657ea-c31d-4543-adbb-c8944e9cafa8",
  "description": None,
  "previous_question_id": None,
  "lesson_id": [
    "ba60aaa7-ff66-4dbe-939c-1a24de54fd37"
  ],
  "lesson_type": [
    3
  ],
  "week_number": None,
  "multiple_choices": 0,
  "question_style_id": None,
  "question_type": 4,
  "question_sub_type": 3,
  "subject_id": "TiengViet_1",
  "subject_name": "Tiếng Việt Lớp 1",
  "difficulty": 1,
  "level": 1,
  "lesson_question_reference_content_id": "",
  "title": "Dựa vào bức tranh sau, em hãy điền từ chọn vào chỗ trống",
  "title_audio_link": None,
  "content": {'type': 'series', 'style': {'display': 'list-item'}, 'value': [{'type': 'html', 'value': 'https://media.trangnguyen.edu.vn/uploads/2019/De%20thi%202023/Do%20vat/minh_la_sach%203x3.png'}, {'type': 'html', 'value': 'Chúng mình là sách. Trong tên chúng mình có vần @[@] @[@].'}], 'list_select': [{'id': '5df0143b590e17567594e4174c4ee8cd', 'list_value': ['test', 'quyển sách', 'ach']}]},
  "body": None,
  "answer": {'style': 0, 'answers_list': [{'id': '4f0df62a417673edbb20e03747d030eb', 'correct_value': ['quyển sách']}, {'id': '85988b6b5bd294e1dbde8d58d56a1b07', 'correct_value': ['sách']}]},
  "collection": [
    "LT"
  ],
  "hint": "",
  "state": 99,
  "lessons": [
    {
      "lesson_id": "ba60aaa7-ff66-4dbe-939c-1a24de54fd37",
      "lesson_name": "test 111 - (Khóa học: Chuyên đề - Tiếng Việt lớp 1)"
    }
  ],
  "text_search": "type:image,value: nhà có mái màu @@ đỏ"
}
    # decode_content_keo_tha_vao_o_trong([data])