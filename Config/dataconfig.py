import os

class TestData:
    """this is base of url"""
    BASE_URL_DEV = "https://accel.id"
    BASE_URL_STAGING = "https://accel_staging.co.id"
    BASE_URL_PROD = "https://accel_prod.co.id"

    """This is General Password"""
    PWD_SUPERADMIN = os.environ.get("PWD_SUPERADMIN")
    INVALID_PASSWORD = "JDJ009"
    BLANK_PASSWORD = ""

    """This is all EMAIL Account Test Data"""
    SUPERADMIN_27 = "visiprimaqa+27@gmail.com"
    JOB_SEEKER_ONLY = ""
    JOB_SEEKER_HRMS_ADMIN = ""
    JOB_SEEKER_HRMS_EMPLOYEE = ""

    JOB_POSTER_ADM_ONLY = ""
    JOB_POSTERADM_HRMS_ADM = ""
    JOB_POSTERADM_HRMS_EMPLOYEE = ""



