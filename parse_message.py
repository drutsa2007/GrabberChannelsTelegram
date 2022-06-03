# Message(id=3293,
# peer_id=PeerChannel(channel_id=1794259776), date=datetime.datetime(2022, 6, 3, 12, 6, 13, tzinfo=datetime.timezone.utc),
# message='Python developer (middle)\n#удаленка #гибрид #полныйдень \nЗ/П от 150 000 до 200 000 ₽\nЛокация: Москва\n\n
# Ищем Python разработчика с опытом в промышленных проектах для разработки внутренних ML / MLOps фреймворков и библиотек
# для ведущего подразделения банка - кредитного скоринга\n\nЗадачи:\n- разработка внутренних программных библиотек и фреймворков,
# использующих ML (написание качественного объектно-ориентированного кода, документации, юнит-тестов)\n- написание CI/CD
# пайплайнов для автоматизации юнит-тестирования, проверки code style, генерации документации\n- участие в доработке
# Python-инструментов для автоматизации ETL на SQL (DataOps)\n- участие в развитии MLOps-инструментов (доработка их
# компонент, настройка)\n\nТребования:\n- опыт разработки на Python в больших и сложных проектах в роли ведущего разработчика
# \n- знание и опыт использования паттернов проектирования\n- знание библиотек Numpy, Pandas, достаточное для быстрого написания
# эффективного кода\n- опыт и понимание принципов параллельного программирования\n- знание и опыт использования Git\n- понимание
# принципов работы операционной системы. Знание основ и опыт использования ОС Linux (Bash)\n- знание и опыт использования SQL
# (можно без процедурных расширений)\n\nБудет плюсом:\n- знание основ машинного обучения, опыт практического применения
# библиотек машинного обучения, например, Scikit-learn, XGBoost, Lightgbm, Catboost\n- понимание принципов написания легковесных
# клиент-серверных приложений на python, реализующих функционал интерактивных дешбордов, опыт использования релевантных
# технологий, например, Flask, Dash, Streamlit\n- знание Docker, Docker-compose или других технологий виртуализации\n- опыт
# настройки CI/CD конвейеров\n- опыт работы с библиотеками визуализации данных (например, Plotly, Matplotlib)\n- опыт
# использования технологий big data\n- опыт использования MLOps-инструментов (например, Kedro, DVCd, MLFlow, Seldon)\n-
# свой open source проект, contribution в известные open source проекты, свой проект, которым можете похвастаться\n\n#
# вакансия #IT #devs #developer #django #python #sql #middle',
#
# out=False, mentioned=False, media_unread=False, silent=False, post=False, from_scheduled=False, legacy=False,
# edit_hide=True, pinned=True, from_id=PeerChannel(channel_id=1292405242),
# fwd_from=MessageFwdHeader(date=datetime.datetime(2022, 6, 3, 12, 6, 10, tzinfo=datetime.timezone.utc),
# imported=False, from_id=PeerChannel(channel_id=1292405242), from_name=None, channel_post=1465, post_author=None,
# saved_from_peer=PeerChannel(channel_id=1292405242), saved_from_msg_id=1465, psa_type=None), via_bot_id=None,
# reply_to=None, media=None,
# reply_markup=ReplyInlineMarkup(rows=[KeyboardButtonRow(buttons=[KeyboardButtonUrl(text='✅ откликнуться',
# url='https://getmatch.ru/vacancies/9032?s=offers')])]), entities=[MessageEntityHashtag(offset=26, length=9),
# MessageEntityHashtag(offset=36, length=7), MessageEntityHashtag(offset=44, length=11), MessageEntityBold(offset=57, length=35),
# MessageEntityBold(offset=94, length=8), MessageEntityBold(offset=277, length=8), MessageEntityBold(offset=714, length=12),
# MessageEntityBold(offset=1219, length=14), MessageEntityHashtag(offset=2005, length=9), MessageEntityHashtag(offset=2015, length=3),
# MessageEntityHashtag(offset=2019, length=5), MessageEntityHashtag(offset=2025, length=10), MessageEntityHashtag(offset=2036, length=7),
# MessageEntityHashtag(offset=2044, length=7), MessageEntityHashtag(offset=2052, length=4), MessageEntityHashtag(offset=2057, length=7)],
# views=440, forwards=1, replies=MessageReplies(replies=0, replies_pts=5909, comments=False, recent_repliers=[], channel_id=None,
# max_id=None, read_max_id=None), edit_date=datetime.datetime(2022, 6, 3, 12, 35, 6, tzinfo=datetime.timezone.utc), post_author=None,
# grouped_id=None, restriction_reason=[], ttl_period=None)

from aiogram import Bot, Dispatcher, executor, types
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

bot = Bot(token=config['Telegram']['API_TOKEN'])
GROUP_ID = -653256393  # Ваш ID группы
#bot.send_message(GROUP_ID, "Сообщение")
#bot.polling()



# https://t.me/python_cool/3293
async def parse_message(message, url):
    url_post = url + '/' + str(message.id)
    with open('last_post.txt', 'w') as f:
        f.write(str(message.id))
    # print(message.message)
    if (message.message != 'None'):
        await bot.send_message(GROUP_ID, url_post)
