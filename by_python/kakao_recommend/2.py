import requests


def avgRotorSpeed(statusQuery, parentId):
    url = f"https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}"
    res = requests.get(url).json()
    pages = res["total_pages"]
    how_many = 0
    total = 0
    for page in range(1, pages + 1):
        running_data = requests.get(url + f"&page={page}").json()["data"]
        for each in running_data:
            if (
                "parent" in each
                and each["parent"] != None
                and "id" in each["parent"]
                and each["parent"]["id"] == parentId
            ):
                how_many += 1
                total += each["operatingParams"]["rotorSpeed"]

    if how_many:
        return total // how_many
    else:
        return 0


if __name__ == "__main__":
    q = "RUNNING"
    p = 7
    print(avgRotorSpeed(q, p))
