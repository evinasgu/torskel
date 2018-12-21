import tornado.web
from torskel.torskel_app import TorskelServer
from torskel.torskel_handler import TorskelHandler
import jwt
from tornado.options import options
from torskel.libs.auth.jwt import jwtauth


options.define("secret_key", "#MY_SeCrEt_KEy",
               type=str)


class HelloJwtLoginHandler(TorskelHandler):

    async def check_passwd(self, user, password):
        return True

    async def post(self):

        user = self.get_argument('username')
        psw = self.get_argument('username')
        if await self.check_passwd(user, psw):
            encoded = jwt.encode({
                'username': user,
            },
            options.secret_key,
                algorithm='HS256'
            )
            response = {'access': encoded.decode("utf-8")}
            self.set_header('Content-Type', 'application/javascript')
            self.write(response)
            self.finish()
        else:
            raise tornado.web.HTTPError(403, 'invalid username')


@jwtauth
class HelloJwtSecuredHandler(TorskelHandler):
    def get(self):
        self.write('Hello, auth success')


hello_app = TorskelServer(handlers=[(r"/login", HelloJwtLoginHandler),
                                    (r"/secured", HelloJwtSecuredHandler)])

if __name__ == '__main__':
    hello_app.init_srv()
    tornado.ioloop.IOLoop.current().start()