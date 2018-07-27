from aiohttp import web


async def main_page(request):
    return web.Response(body=request.app.main_html, content_type='text/html')


async def stat(request):
    leaderboard = request.app.kaggle_api.competition_leaderboard_view('asasssa')

    result = []
    for i in leaderboard:
        result.append(
            {
                'score': i.score,
                'submission_date': i.submissionDate,
                'name': i.teamName,
            }
        )
    return result
