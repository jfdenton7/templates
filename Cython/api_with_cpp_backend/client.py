import requests as req


if __name__ == '__main__':
    url = 'http://localhost:3030/api/add'
    package = {
        'x': 3,
        'y': 2,
    }

    resp = req.post(
        url, 
        data=package
    )

    print(resp.status_code, resp.reason)
    print(resp.content)
