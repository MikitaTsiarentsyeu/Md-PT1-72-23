class MyError(Exception):

    def __init__(self, message, error_type, error_code) -> None:
        super().__init__(message)
        self.error_type = error_type
        self.error_code = error_code
        self.message_text = message

    def __str__(self) -> str:
        return f"An error of type {self.error_type} ({self.error_code}) occured - {self.message_text}"

try:
    raise MyError("some specific error", "severe error", "303")
except MyError as e:
    print(e)
