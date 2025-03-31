from enum import IntEnum

class HTTPStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

def handle_http(status: HTTPStatus):
    if status == HTTPStatus.OK:
        print("Request was successful.")
    elif status == HTTPStatus.NOT_FOUND:
        print("Resource not found.")
    elif status == HTTPStatus.INTERNAL_SERVER_ERROR:
        print("Internal server error.")
    else:
        print("Unknown status.")

if __name__ == "__main__":
    handle_http(HTTPStatus.OK)
    handle_http(HTTPStatus.NOT_FOUND)