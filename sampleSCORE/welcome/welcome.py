from iconservice import *

TAG = 'Welcome'


class Welcome(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @eventlog(indexed=3)
    def Scrooge(self, _to: Address, _amount: int, _scrooge_get: int, _will_sent: int) -> None:
        pass

    @external(readonly=True)
    def welcome(self) -> str:
        return f"Hello, {self.msg.sender} !!! Welcome to ICON Workshop 2019!!!"

    @external
    def scrooge(self, _to: Address, _amount: int) -> str:

        # check sender's balance is bigger than send value
        if (self.icx.get_balance(self.msg.sender) < _amount):
            self.revert(f"Hey, {self.msg.sender} !!! you have only {self.icx.get_balance(self.msg.sender)} !!!")

        # calculate scrooge's fee
        _scrooge_get = int(_amount/2)
        _will_sent = _amount - _scrooge_get

        self.icx.send(addr_to=_to, amount= _will_sent)

        # write eventlog
        self.Scrooge(self, _to , _amount, _scrooge_get, _will_sent)

        return f" I especially discounted you a commission. \n the fee was {_scrooge_get} \n so, {_will_sent} sent to {_to}"

