import random

from faker import Faker

faker = Faker(locale='zh_CN')
def random_int() -> int:
    """
    :return: 随机数
    """
    _data = random.randint(0, 5000)
    return _data


def get_phone() -> int:
    """
    :return: 随机生成手机号码
    """
    phone = faker.phone_number()
    return phone


def get_id_number() -> int:
    """

    :return: 随机生成身份证号码
    """

    id_number = faker.ssn()
    return id_number


def get_female_name() -> str:
    """

    :return: 女生姓名
    """
    female_name = faker.name_female()
    return female_name


def get_male_name() -> str:
    """

    :return: 男生姓名
    """
    male_name = faker.name_male()
    return male_name


def get_email() -> str:
    """

    :return: 生成邮箱
    """
    email = faker.email()
    return email
if __name__ == '__main__':
    print(get_email())