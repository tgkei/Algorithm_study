import pip._vendor.requests as requests
from pprint import pprint


def avgRotorSpeed(statusQuery, parentId):
    URL = "https://jsonmock.hackerrank.com/api/iot_devices/search"
    params = {"status": statusQuery}
    res = requests.get(URL, params=params).json()

    cnt = res["total_pages"]

    total_cnt = 0
    answer = 0

    for page in range(1, cnt + 1):
        params = {"page": page, "status": statusQuery}
        datas = requests.get(URL, params=params).json()["data"]

        for data in datas:
            if (
                "parent" in data
                and data["parent"] != None
                and "id" in data["parent"]
                and data["parent"]["id"] == parentId
            ):
                total_cnt += 1
                answer += data["operatingParams"]["rotorSpeed"]

    if total_cnt:
        return answer // total_cnt
    else:
        return 0


if __name__ == "__main__":
    statusQuery = "RUNNING"
    parentId = 7
    print(avgRotorSpeed(statusQuery, parentId))
