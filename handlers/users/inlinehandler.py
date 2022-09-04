from loader import dp,db
from aiogram.types import InlineQuery, InlineQueryResultArticle,InputMessageContent

async def queryResult(data):
    query_result=[]
    for id,title,link in data:
        query_result.append(
            InlineQueryResultArticle(
                id=id,
                title=title,
                input_message_content=InputMessageContent(
                    message_text=f"<b>Rust Docs:</b> <a href='https://doc.rust-lang.org/book/{link}'>{title}</a>",
                    parse_mode="HTML"
                ),
                url=f"https://doc.rust-lang.org/book/{link}",
                thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Rust_programming_language_black_logo.svg/1024px-Rust_programming_language_black_logo.svg.png",
                description=f"https://doc.rust-lang.org/book/{link}"
            )
        )

    return query_result

@dp.inline_handler()
async def anyQuery(query: InlineQuery):
    try:
        data=await db.SearchQuery(query.query)
        await query.answer(
            results=await queryResult(data=data)
        )
    except Exception as e:
        await query.answer(
            results=[
                InlineQueryResultArticle(
                    id="001",
                    title="Search RUST lang Documentation 🔍",
                    input_message_content=InputMessageContent(
                        message_text="Query Not Found"
                    ),
                    url=f"https://doc.rust-lang.org/book/",
                    thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Rust_programming_language_black_logo.svg/1024px-Rust_programming_language_black_logo.svg.png",
                    description=f"https://doc.rust-lang.org/book/"
                )
            ]
        )
    