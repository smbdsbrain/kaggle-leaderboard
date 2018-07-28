import datetime

import pytz
from aiohttp import web


async def main_page(request):
    return web.Response(body=request.app.main_html, content_type='text/html')


async def stat(request):
    leaderboard = request.app.kaggle_api.competition_leaderboard_view(
        request.app.context.config.kaggle.competition
    )

    result = []
    for i in leaderboard:
        result.append(
            {
                'score': i.score,
                'submission_date': i.submissionDate.replace(
                        tzinfo=pytz.utc
                    ).astimezone(
                        pytz.timezone(
                            request.app.context.config.timezone
                        )
                    ).strftime('%m-%d %H:%M:%S'),
                'name': i.teamName,
            }
        )
    return result
