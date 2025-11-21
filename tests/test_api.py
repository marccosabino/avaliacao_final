import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_root_and_docs():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        r = await ac.get('/')
        assert r.status_code == 200
        r2 = await ac.get('/docs')
        assert r2.status_code in (200, 307)


@pytest.mark.asyncio
async def test_recommendations_exist():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        r = await ac.get('/recommendations/1?n=5')
        assert r.status_code == 200
        body = r.json()
        assert 'recommendations' in body