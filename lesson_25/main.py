# import os


# USER = os.getenv("USER")
# TOKEN = os.getenv("TOKEN")

# print(USER)
# print(TOKEN)

# print(type(USER))
# print(type(TOKEN))

# import os

# os.environ["password"] = "you_will_never_find_out"

# print(os.getenv("password"))

# import os

# USER = os.environ.get("USER", "Not Set")
# print(USER)

# from typing import Optional


# from pydantic import BaseSettings, IPvAnyAddress


# class Settings(BaseSettings):
#     MONGODB_URL: str = ""
#     API_V1_STR: str = "/api/v1"
#     GF_API_URL: Optional[str] = None
#     TOKEN_SECRET_KEY: str = "fj0823t8y3t9shoidn9184h13iudhaslidfuh3190841-00=52394hfu"


# settings = Settings()

# print(settings.MONGODB_URL)
