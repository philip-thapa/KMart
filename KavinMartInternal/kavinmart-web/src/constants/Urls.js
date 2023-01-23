export class Urls {
    static HOST = 'http://0.0.0.0:8002/';
    static STORE_USER_API_PREFIX = Urls.HOST + 'api/store-users/';

    // STORE USER
    static STORE_USER_SIGN_UP = Urls.STORE_USER_API_PREFIX + 'store-users/signup';
    static STORE_USER_LOGIN = Urls.STORE_USER_API_PREFIX + 'account/token';
}