from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.filters import Command

from handlers import payment

bot = Bot("8063915434:AAFzC7TxH-918uuoUx3tMcDDXhRQswdvCJo")
dp = Dispatcher()

def start():
    # Тут регистрируем обработчики

    dp.message.register(payment.send_invoice_handler, Command(commands="donate"))
    dp.pre_checkout_query.register(payment.pre_checkout_handler)
    dp.message.register(payment.success_payment_handler, F.successful_payment)
    dp.message.register(payment.pay_support_handler, Command(commands="paysupport"))

async def main():
    start()
    await dp.start_polling(bot)
