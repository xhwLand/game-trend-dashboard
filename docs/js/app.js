// 游戏榜单分析看板 - JavaScript

// 全局变量
let allData = {
    douyin: null,
    wechat: null,
    ios_us: null,
    google_us: null
};
let currentPlatform = 'all';
let trendChart = null;
let typeChart = null;
let platformChart = null;

// 平台名称映射
const platformNames = {
    'douyin': '抖音小游戏',
    'wechat': '微信小游戏',
    'ios_us': 'iOS美区',
    'google_us': 'Google美区'
};

// 初始化
document.addEventListener('DOMContentLoaded', function() {
    loadAllData();
});

// 加载所有数据
async function loadAllData() {
    const updateElement = document.getElementById('lastUpdate');
    updateElement.textContent = '正在加载数据...';
    
    try {
        // 并行加载所有平台数据
        const promises = [
            fetchData('douyin'),
            fetchData('wechat'),
            fetchData('ios_us'),
            fetchData('google_us')
        ];
        
        await Promise.all(promises);
        
        // 更新显示
        updateLastUpdate();
        updateStats();
        renderCharts();
        renderTable();
        
        console.log('数据加载完成!');
    } catch (error) {
        console.error('数据加载失败:', error);
        updateElement.textContent = '数据加载失败，请刷新重试';
    }
}

// 获取单个平台数据
async function fetchData(platform) {
    try {
        const response = await fetch(`data/${platform}/latest.json`);
        if (response.ok) {
            allData[platform] = await response.json();
        } else {
            // 如果没有数据，使用示例数据
            allData[platform] = getSampleData(platform);
        }
    } catch (error) {
        console.log(`${platform} 数据加载失败，使用示例数据`);
        allData[platform] = getSampleData(platform);
    }
}

// 示例数据（当API不可用时）
function getSampleData(platform) {
    const today = new Date().toISOString().split('T')[0];
    const games = generateSampleGames(platform);
    
    return {
        platform: platformNames[platform],
        update_date: today,
        update_time: new Date().toISOString(),
        count: games.length,
        games: games
    };
}

// 生成示例游戏数据
function generateSampleGames(platform) {
    const gameTemplates = {
        'douyin': [
            { name: '贪吃蛇大作战', type: '休闲', baseScore: 9800 },
            { name: '消灭星星', type: '益智', baseScore: 9700 },
            { name: '跳一跳', type: '休闲', baseScore: 9600 },
            { name: '植物大战僵尸2', type: '策略', baseScore: 9500 },
            { name: '保卫萝卜', type: '塔防', baseScore: 9400 },
            { name: '开心消消乐', type: '消除', baseScore: 9300 },
            { name: '球球大作战', type: '休闲', baseScore: 9200 },
            { name: '穿越火线', type: '射击', baseScore: 9100 },
            { name: '王者荣耀', type: 'MOBA', baseScore: 9000 },
            { name: '和平精英', type: '射击', baseScore: 8900 },
        ],
        'wechat': [
            { name: '跳一跳', type: '休闲', baseScore: 9900 },
            { name: '欢乐斗地主', type: '棋牌', baseScore: 9800 },
            { name: '欢乐麻将', type: '棋牌', baseScore: 9700 },
            { name: '天天象棋', type: '棋牌', baseScore: 9600 },
            { name: '腾讯欢乐捕鱼', type: '休闲', baseScore: 9500 },
            { name: '拳皇命运', type: '动作', baseScore: 9400 },
            { name: '火柴人战争', type: '策略', baseScore: 9300 },
            { name: '植物大战僵尸', type: '塔防', baseScore: 9200 },
            { name: '保卫萝卜', type: '塔防', baseScore: 9100 },
            { name: '开心消消乐', type: '消除', baseScore: 9000 },
        ],
        'ios_us': [
            { name: 'Subway Surfers', type: 'Runner', baseScore: 4.7 },
            { name: 'Candy Crush Saga', type: 'Puzzle', baseScore: 4.6 },
            { name: 'Temple Run', type: 'Runner', baseScore: 4.5 },
            { name: 'Among Us', type: 'Party', baseScore: 4.8 },
            { name: 'Roblox', type: 'Adventure', baseScore: 4.5 },
            { name: 'Geometry Dash', type: 'Rhythm', baseScore: 4.7 },
            { name: 'Hill Climb Racing', type: 'Racing', baseScore: 4.6 },
            { name: 'Monopoly GO!', type: 'Board', baseScore: 4.4 },
            { name: 'PUBG Mobile', type: 'Shooter', baseScore: 4.5 },
            { name: 'Minecraft', type: 'Sandbox', baseScore: 4.8 },
        ],
        'google_us': [
            { name: 'Subway Surfers', type: 'Runner', baseScore: 4.7 },
            { name: 'Candy Crush Saga', type: 'Puzzle', baseScore: 4.6 },
            { name: 'Temple Run', type: 'Runner', baseScore: 4.5 },
            { name: 'Among Us', type: 'Party', baseScore: 4.8 },
            { name: 'Roblox', type: 'Adventure', baseScore: 4.5 },
            { name: 'Geometry Dash', type: 'Rhythm', baseScore: 4.7 },
            { name: 'Hill Climb Racing', type: 'Racing', baseScore: 4.6 },
            { name: 'Monopoly GO!', type: 'Board', baseScore: 4.4 },
            { name: 'PUBG Mobile', type: 'Shooter', baseScore: 4.5 },
            { name: 'Minecraft', type: 'Sandbox', baseScore: 4.8 },
        ]
    };
    
    const templates = gameTemplates[platform] || gameTemplates['douyin'];
    const trends = ['up', 'up', 'stable', 'down'];
    
    return templates.map((game, index) => ({
        rank: index + 1,
        name: game.name,
        type: game.type,
        score: game.baseScore - (index * 50) + (Math.random() * 20 - 10),
        trend: trends[Math.floor(Math.random() * trends.length)],
        potential: game.baseScore > 9500 ? 'high' : (game.baseScore > 9200 ? 'medium' : 'low')
    }));
}

// 更新最后更新时间
function updateLastUpdate() {
    const now = new Date();
    const updateStr = now.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    });
    document.getElementById('lastUpdate').textContent = `最后更新: ${updateStr}`;
}

// 更新统计卡片
function updateStats() {
    let totalGames = 0;
    let topGame = '';
    let topScore = 0;
    let trendingUp = 0;
    let totalRating = 0;
    let ratingCount = 0;
    
    for (const platform in allData) {
        const data = allData[platform];
        if (data && data.games) {
            totalGames += data.count;
            
            data.games.forEach(game => {
                if (game.score > topScore) {
                    topScore = game.score;
                    topGame = game.name;
                }
                if (game.trend === 'up') {
                    trendingUp++;
                }
                if (game.score > 5) { // 评分制
                    totalRating += game.score;
                    ratingCount++;
                }
            });
        }
    }
    
    document.getElementById('totalGames').textContent = totalGames;
    document.getElementById('topGame').textContent = topGame.length > 10 ? topGame.substring(0, 10) + '...' : topGame;
    document.getElementById('trendingUp').textContent = trendingUp;
    document.getElementById('avgRating').textContent = ratingCount > 0 ? (totalRating / ratingCount).toFixed(1) : '-';
}

// 切换平台
function switchPlatform(platform) {
    currentPlatform = platform;
    
    // 更新标签样式
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.platform === platform) {
            btn.classList.add('active');
        }
    });
    
    // 更新筛选器
    document.getElementById('platformFilter').value = platform;
    
    // 重新渲染表格
    renderTable();
}

// 渲染图表
function renderCharts() {
    // 热度趋势图
    const trendCtx = document.getElementById('trendChart').getContext('2d');
    if (trendChart) trendChart.destroy();
    
    const labels = ['1-10', '11-20', '21-30', '31-40', '41-50'];
    const datasets = [];
    
    const colors = ['#ef4444', '#f59e0b', '#10b981', '#6366f1'];
    let colorIndex = 0;
    
    for (const platform in allData) {
        const data = allData[platform];
        if (data && data.games) {
            const avgScores = calculateAvgByRank(data.games);
            datasets.push({
                label: platformNames[platform],
                data: avgScores,
                borderColor: colors[colorIndex % colors.length],
                backgroundColor: colors[colorIndex % colors.length] + '20',
                tension: 0.4,
                fill: true
            });
            colorIndex++;
        }
    }
    
    trendChart = new Chart(trendCtx, {
        type: 'line',
        data: { labels, datasets },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top' }
            },
            scales: {
                y: { beginAtZero: false }
            }
        }
    });
    
    // 游戏类型分布图
    const typeCtx = document.getElementById('typeChart').getContext('2d');
    if (typeChart) typeChart.destroy();
    
    const typeData = calculateTypeDistribution();
    
    typeChart = new Chart(typeCtx, {
        type: 'doughnut',
        data: {
            labels: Object.keys(typeData),
            datasets: [{
                data: Object.values(typeData),
                backgroundColor: [
                    '#ef4444', '#f59e0b', '#10b981', '#6366f1',
                    '#ec4899', '#8b5cf6', '#06b6d4', '#84cc16'
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'right' }
            }
        }
    });
    
    // 平台分布图
    const platformCtx = document.getElementById('platformChart').getContext('2d');
    if (platformChart) platformChart.destroy();
    
    const platformData = {
        '抖音小游戏': allData.douyin?.count || 0,
        '微信小游戏': allData.wechat?.count || 0,
        'iOS美区': allData.ios_us?.count || 0,
        'Google美区': allData.google_us?.count || 0
    };
    
    platformChart = new Chart(platformCtx, {
        type: 'bar',
        data: {
            labels: Object.keys(platformData),
            datasets: [{
                label: '游戏数量',
                data: Object.values(platformData),
                backgroundColor: ['#ef4444', '#f59e0b', '#10b981', '#6366f1']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// 计算每个排名段的平均分数
function calculateAvgByRank(games) {
    const groups = [
        games.slice(0, 10),
        games.slice(10, 20),
        games.slice(20, 30),
        games.slice(30, 40),
        games.slice(40, 50)
    ];
    
    return groups.map(group => {
        if (group.length === 0) return 0;
        const sum = group.reduce((acc, g) => acc + g.score, 0);
        return (sum / group.length).toFixed(1);
    });
}

// 计算类型分布
function calculateTypeDistribution() {
    const types = {};
    
    for (const platform in allData) {
        const data = allData[platform];
        if (data && data.games) {
            data.games.forEach(game => {
                types[game.type] = (types[game.type] || 0) + 1;
            });
        }
    }
    
    return types;
}

// 渲染表格
function renderTable() {
    const tbody = document.getElementById('gamesTableBody');
    let games = [];
    
    // 收集游戏数据
    for (const platform in allData) {
        const data = allData[platform];
        if (data && data.games) {
            data.games.forEach(game => {
                games.push({
                    ...game,
                    platform: platformNames[platform],
                    platformKey: platform
                });
            });
        }
    }
    
    // 筛选
    if (currentPlatform !== 'all') {
        games = games.filter(g => g.platformKey === currentPlatform);
    }
    
    // 排序
    games.sort((a, b) => a.rank - b.rank);
    
    // 限制显示数量
    games = games.slice(0, 50);
    
    // 渲染
    if (games.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" class="loading">暂无数据</td></tr>';
        return;
    }
    
    tbody.innerHTML = games.map(game => {
        const trendIcon = getTrendIcon(game.trend);
        const potentialBadge = getPotentialBadge(game.potential);
        const scoreDisplay = game.score > 5 ? game.score.toFixed(1) : Math.round(game.score);
        
        return `
            <tr>
                <td><strong>#${game.rank}</strong></td>
                <td>${game.name}</td>
                <td>${game.platform}</td>
                <td>${game.type}</td>
                <td>${scoreDisplay}</td>
                <td class="trend-${game.trend}">${trendIcon}</td>
                <td>${potentialBadge}</td>
            </tr>
        `;
    }).join('');
}

// 获取趋势图标
function getTrendIcon(trend) {
    switch (trend) {
        case 'up': return '📈';
        case 'down': return '📉';
        default: return '➡️';
    }
}

// 获取潜力标签
function getPotentialBadge(potential) {
    switch (potential) {
        case 'high': return '<span class="potential-badge high">高潜力</span>';
        case 'medium': return '<span class="potential-badge medium">中潜力</span>';
        default: return '<span class="potential-badge low">普通</span>';
    }
}

// 筛选表格
function filterTable() {
    const filterValue = document.getElementById('platformFilter').value;
    currentPlatform = filterValue;
    
    // 更新标签
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.platform === filterValue) {
            btn.classList.add('active');
        }
    });
    
    renderTable();
}

// 排序表格
function sortTable() {
    const sortBy = document.getElementById('sortBy').value;
    let games = [];
    
    for (const platform in allData) {
        const data = allData[platform];
        if (data && data.games) {
            data.games.forEach(game => {
                games.push({
                    ...game,
                    platform: platformNames[platform],
                    platformKey: platform
                });
            });
        }
    }
    
    if (currentPlatform !== 'all') {
        games = games.filter(g => g.platformKey === currentPlatform);
    }
    
    switch (sortBy) {
        case 'rank':
            games.sort((a, b) => a.rank - b.rank);
            break;
        case 'score':
            games.sort((a, b) => b.score - a.score);
            break;
        case 'name':
            games.sort((a, b) => a.name.localeCompare(b.name));
            break;
    }
    
    // 更新rank
    games.forEach((game, index) => {
        game.rank = index + 1;
    });
    
    // 重新渲染
    const tbody = document.getElementById('gamesTableBody');
    tbody.innerHTML = games.slice(0, 50).map(game => {
        const trendIcon = getTrendIcon(game.trend);
        const potentialBadge = getPotentialBadge(game.potential);
        const scoreDisplay = game.score > 5 ? game.score.toFixed(1) : Math.round(game.score);
        
        return `
            <tr>
                <td><strong>#${game.rank}</strong></td>
                <td>${game.name}</td>
                <td>${game.platform}</td>
                <td>${game.type}</td>
                <td>${scoreDisplay}</td>
                <td class="trend-${game.trend}">${trendIcon}</td>
                <td>${potentialBadge}</td>
            </tr>
        `;
    }).join('');
}
