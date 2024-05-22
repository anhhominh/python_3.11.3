

from fastapi import HTTPException


async def update_multi_schools():
    # ans = []
    # try:
    #     contents = file.file.read()
    # except Exception:
    #     raise HTTPException(
    #         status_code= 500,
    #         detail='There was an error uploading the file',
    #     )
    # finally:
    #     await file.close()

    list_school = str(contents,'utf-8').split("\r\n")
    for i in list_school:
        print(len(i.split("|")))
        # answer = update_school(i)
        # ans.append(answer)
    # logger.info(ans)

if __name__ == "__main__":
    update_multi_schools()