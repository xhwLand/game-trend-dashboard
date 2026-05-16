// 娓告垙姒滃崟鍒嗘瀽鐪嬫澘 - JavaScript

// 鍏ㄥ眬鍙橀噺
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

// 骞冲彴鍚嶇О鏄犲皠
const platformNames = {
    'douyin': '鎶栭煶灏忔父鎴?,
    'wechat': '寰俊灏忔父鎴?,
    'ios_us': 'iOS缇庡尯',
    'google_us': 'Google缇庡尯'
};

// 鍒濆鍖?document.addEventListener('DOMContentLoaded', function() {
    loadAllData();
});

// 鍔犺浇鎵€鏈夋暟鎹?async function loadAllData() {
    const updateElement = document.getElementById('lastUpdate');
    updateElement.textContent = '姝ｅ湪鍔犺浇鏁版嵁...';
    
    try {
        // 骞惰鍔犺浇鎵€鏈夊钩鍙版暟鎹?        const promises = [
            fetchData('douyin'),
            fetchData('wechat'),
            fetchData('ios_us'),
            fetchData('google_us')
        ];
        
        await Promise.all(promises);
        
        // 鏇存柊鏄剧ず
        updateLastUpdate();
        updateStats();
        renderCharts();
        renderTable();
        
        console.log('鏁版嵁鍔犺浇瀹屾垚!');
    } catch (error) {
        console.error('鏁版嵁鍔犺浇澶辫触:', error);
        updateElement.textContent = '鏁版嵁鍔犺浇澶辫触锛岃鍒锋柊閲嶈瘯';
    }
}

// 鑾峰彇鍗曚釜骞冲彴鏁版嵁
async function fetchData(platform) {
    try {
        const response = await fetch(`data/${platform}/latest.json`);
        if (response.ok) {
            allData[platform] = await response.json();
        } else {
            // 濡傛灉娌℃湁鏁版嵁锛屼娇鐢ㄧず渚嬫暟鎹?            allData[platform] = getSampleData(platform);
        }
    } catch (error) {
        console.log(`${platform} 鏁版嵁鍔犺浇澶辫触锛屼娇鐢ㄧず渚嬫暟鎹甡);
        allData[platform] = getSampleData(platform);
    }
}

// 绀轰緥鏁版嵁锛堝綋API涓嶅彲鐢ㄦ椂锛?function getSampleData(platform) {
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

// 鐢熸垚绀轰緥娓告垙鏁版嵁
function generateSampleGames(platform) {
    const gameTemplates = {
        'douyin': [
            { name: '璐悆铔囧ぇ浣滄垬', type: '浼戦棽', baseScore: 9800 },
            { name: '娑堢伃鏄熸槦', type: '鐩婃櫤', baseScore: 9700 },
            { name: '璺充竴璺?, type: '浼戦棽', baseScore: 9600 },
            { name: '妞嶇墿澶ф垬鍍靛案2', type: '绛栫暐', baseScore: 9500 },
            { name: '淇濆崼钀濆崪', type: '濉旈槻', baseScore: 9400 },
            { name: '寮€蹇冩秷娑堜箰', type: '娑堥櫎', baseScore: 9300 },
            { name: '鐞冪悆澶т綔鎴?, type: '浼戦棽', baseScore: 9200 },
            { name: '绌胯秺鐏嚎', type: '灏勫嚮', baseScore: 9100 },
            { name: '鐜嬭€呰崳鑰€', type: 'MOBA', baseScore: 9000 },
            { name: '鍜屽钩绮捐嫳', type: '灏勫嚮', baseScore: 8900 },
        ],
        'wechat': [
            { name: '璺充竴璺?, type: '浼戦棽', baseScore: 9900 },
            { name: '娆箰鏂楀湴涓?, type: '妫嬬墝', baseScore: 9800 },
            { name: '娆箰楹诲皢', type: '妫嬬墝', baseScore: 9700 },
            { name: '澶╁ぉ璞℃', type: '妫嬬墝', baseScore: 9600 },
            { name: '鑵捐娆箰鎹曢奔', type: '浼戦棽', baseScore: 9500 },
            { name: '鎷崇殗鍛借繍', type: '鍔ㄤ綔', baseScore: 9400 },
            { name: '鐏煷浜烘垬浜?, type: '绛栫暐', baseScore: 9300 },
            { name: '妞嶇墿澶ф垬鍍靛案', type: '濉旈槻', baseScore: 9200 },
            { name: '淇濆崼钀濆崪', type: '濉旈槻', baseScore: 9100 },
            { name: '寮€蹇冩秷娑堜箰', type: '娑堥櫎', baseScore: 9000 },
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

// 鏇存柊鏈€鍚庢洿鏂版椂闂?function updateLastUpdate() {
    const now = new Date();
    const updateStr = now.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    });
    document.getElementById('lastUpdate').textContent = `鏈€鍚庢洿鏂? ${updateStr}`;
}

// 鏇存柊缁熻鍗＄墖
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
                if (game.score > 5) { // 璇勫垎鍒?                    totalRating += game.score;
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

// 鍒囨崲骞冲彴
function switchPlatform(platform) {
    currentPlatform = platform;
    
    // 鏇存柊鏍囩鏍峰紡
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.platform === platform) {
            btn.classList.add('active');
        }
    });
    
    // 鏇存柊绛涢€夊櫒
    document.getElementById('platformFilter').value = platform;
    
    // 閲嶆柊娓叉煋琛ㄦ牸
    renderTable();
}

// 娓叉煋鍥捐〃
function renderCharts() {
    // 鐑害瓒嬪娍鍥?    const trendCtx = document.getElementById('trendChart').getContext('2d');
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
    
    // 娓告垙绫诲瀷鍒嗗竷鍥?    const typeCtx = document.getElementById('typeChart').getContext('2d');
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
    
    // 骞冲彴鍒嗗竷鍥?    const platformCtx = document.getElementById('platformChart').getContext('2d');
    if (platformChart) platformChart.destroy();
    
    const platformData = {
        '鎶栭煶灏忔父鎴?: allData.douyin?.count || 0,
        '寰俊灏忔父鎴?: allData.wechat?.count || 0,
        'iOS缇庡尯': allData.ios_us?.count || 0,
        'Google缇庡尯': allData.google_us?.count || 0
    };
    
    platformChart = new Chart(platformCtx, {
        type: 'bar',
        data: {
            labels: Object.keys(platformData),
            datasets: [{
                label: '娓告垙鏁伴噺',
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

// 璁＄畻姣忎釜鎺掑悕娈电殑骞冲潎鍒嗘暟
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

// 璁＄畻绫诲瀷鍒嗗竷
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

// 娓叉煋琛ㄦ牸
function renderTable() {
    const tbody = document.getElementById('gamesTableBody');
    let games = [];
    
    // 鏀堕泦娓告垙鏁版嵁
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
    
    // 绛涢€?    if (currentPlatform !== 'all') {
        games = games.filter(g => g.platformKey === currentPlatform);
    }
    
    // 鎺掑簭
    games.sort((a, b) => a.rank - b.rank);
    
    // 闄愬埗鏄剧ず鏁伴噺
    games = games.slice(0, 50);
    
    // 娓叉煋
    if (games.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" class="loading">鏆傛棤鏁版嵁</td></tr>';
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

// 鑾峰彇瓒嬪娍鍥炬爣
function getTrendIcon(trend) {
    switch (trend) {
        case 'up': return '馃搱';
        case 'down': return '馃搲';
        default: return '鉃★笍';
    }
}

// 鑾峰彇娼滃姏鏍囩
function getPotentialBadge(potential) {
    switch (potential) {
        case 'high': return '<span class="potential-badge high">楂樻綔鍔?/span>';
        case 'medium': return '<span class="potential-badge medium">涓綔鍔?/span>';
        default: return '<span class="potential-badge low">鏅€?/span>';
    }
}

// 绛涢€夎〃鏍?function filterTable() {
    const filterValue = document.getElementById('platformFilter').value;
    currentPlatform = filterValue;
    
    // 鏇存柊鏍囩
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.platform === filterValue) {
            btn.classList.add('active');
        }
    });
    
    renderTable();
}

// 鎺掑簭琛ㄦ牸
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
    
    // 鏇存柊rank
    games.forEach((game, index) => {
        game.rank = index + 1;
    });
    
    // 閲嶆柊娓叉煋
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
