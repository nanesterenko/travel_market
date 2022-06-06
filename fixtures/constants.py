"""Константы, в т.ч. тексты ошибок и уведомлений."""


class Notice:
    ERROR_DIFFERENT_PASSWORD = "The two password fields didn’t match."
    ERROR_TOO_SHORT_PASSWORD = "This password is too short. It must contain at least 8 characters."
    ERROR_TOO_COMMON_PASSWORD = "This password is too common."
    ERROR_ONLY_NUMERIC_PASSWORD = "This password is entirely numeric."
    ERROR_EXIST_USER = "A user with that username already exists."
    ERROR_USERNAME_LIKE_PASSWORD = "The password is too similar to the username."
    ERROR_INVALID_EMAIL = "Enter a valid email address."
    ERROR_INVALID_AGE = "You are young!"
    ERROR_NON_EXIST_USER = "Please enter a correct username and password. Note that both fields may be case-sensitive."
    ERROR_UPLOAD_AVATAR = "Upload a valid image. The file you uploaded was either not an image or a corrupted image."
    ERROR_UPLOAD_EMPTY_FILE = "The submitted file is empty."