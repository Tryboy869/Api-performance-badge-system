<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RapidAPI - POC Badges de Performance</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    
    <style>
        :root {
            --rapidapi-blue: #0066CC;
            --rapidapi-dark-blue: #004c99;
            --light-gray: #F5F7FA;
            --medium-gray: #E1E8ED;
            --dark-gray: #5A738E;
            --text-color: #111827;
            --text-light: #6B7280;
            --white: #FFFFFF;
            --premium-gold: #FFD700;
            --premium-gold-dark: #daa520;
            --premium-revenue-color: #0d874b;

            /* Badge Colors */
            --badge-trusted-bg: #E6F4EA;
            --badge-trusted-text: #0A7D37;
            --badge-fast-bg: #FFF4E5;
            --badge-fast-text: #FF8A00;
            --badge-blazing-bg: #FFECEB;
            --badge-blazing-text: #E53935;
            --badge-enterprise-bg: #EBF5FF;
            --badge-enterprise-text: #0052CC;
            --badge-community-bg: #F3E8FF;
            --badge-community-text: #6A1B9A;
            --badge-downtime-bg: linear-gradient(135deg, #FFD700, #F0B400);
            --badge-downtime-text: #4C3D00;
            --badge-security-bg: #F1F3F5;
            --badge-security-text: #212529;
            --badge-volume-bg: #D4EDDA;
            --badge-volume-text: #155724;
        }

        /* --- Global & Reset --- */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--light-gray);
            color: var(--text-color);
            line-height: 1.6;
        }
        
        /* --- Loader --- */
        .loader-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 50vh;
        }
        .loader {
            border: 5px solid #f3f3f3;
            border-top: 5px solid var(--rapidapi-blue);
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }


        /* --- Main Layout (Mobile First) --- */
        .poc-container {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        .main-wrapper {
            display: flex;
            flex-grow: 1;
        }

        /* --- Header --- */
        .header {
            background-color: var(--white);
            padding: 0.75rem 1rem;
            border-bottom: 1px solid var(--medium-gray);
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .header-logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--rapidapi-blue);
            text-decoration: none;
        }
        .header-logo i { margin-right: 8px; }
        .mobile-menu-toggle {
            display: block;
            font-size: 1.5rem;
            background: none;
            border: none;
            cursor: pointer;
            color: var(--rapidapi-blue);
        }

        /* --- Sidebar (Hidden on Mobile by default) --- */
        .sidebar {
            position: fixed;
            top: 0;
            left: 0;
            width: 280px;
            height: 100%;
            background-color: var(--white);
            border-right: 1px solid var(--medium-gray);
            padding: 1.5rem 1rem;
            transform: translateX(-100%);
            transition: transform 0.3s ease-in-out;
            z-index: 1100;
            overflow-y: auto;
        }
        .sidebar.is-open {
            transform: translateX(0);
        }
        .sidebar-close-btn {
            position: absolute;
            top: 10px;
            right: 15px;
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
        }
        .sidebar-section { margin-bottom: 2rem; }
        .sidebar-title {
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            color: var(--text-light);
            margin-bottom: 1rem;
            letter-spacing: 0.5px;
        }
        .filter-list { list-style: none; }
        .filter-item { margin-bottom: 0.5rem; }
        .filter-item a {
            display: block;
            text-decoration: none;
            color: var(--dark-gray);
            padding: 0.5rem;
            border-radius: 6px;
            transition: background-color 0.2s, color 0.2s;
        }
        .filter-item a:hover {
            background-color: var(--light-gray);
            color: var(--rapidapi-blue);
        }
        #badge-filters .filter-item a {
            display: flex;
            align-items: center;
            font-size: 0.9rem;
            cursor: pointer;
            border: 1px solid transparent;
        }
        #badge-filters .filter-item a.active {
            background-color: var(--badge-enterprise-bg);
            color: var(--badge-enterprise-text);
            font-weight: 600;
            border: 1px solid var(--badge-enterprise-text);
        }
        .badge-filter-icon { 
            width: 28px;
            height: 28px;
            display: inline-flex;
            justify-content: center;
            align-items: center;
            margin-right: 10px;
            font-size: 0.8rem;
            border-radius: 4px;
        }

        /* --- Main Content --- */
        .main-content {
            flex-grow: 1;
            padding: 1rem;
            width: 100%;
        }

        .content-header {
            margin-bottom: 1.5rem;
        }
        .search-bar-wrapper {
            position: relative;
            margin-bottom: 1rem;
        }
        .search-bar-wrapper i {
            position: absolute;
            left: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-light);
        }
        #search-input {
            width: 100%;
            padding: 0.75rem 1rem 0.75rem 2.5rem;
            border: 1px solid var(--medium-gray);
            border-radius: 8px;
            font-size: 1rem;
        }
        #search-input:focus {
            outline: none;
            border-color: var(--rapidapi-blue);
            box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.2);
        }

        .controls-wrapper {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        
        .toggle-switch {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .toggle-switch label { cursor: pointer; }
        .switch {
            position: relative;
            display: inline-block;
            width: 44px;
            height: 24px;
        }
        .switch input { opacity: 0; width: 0; height: 0; }
        .slider {
            position: absolute;
            cursor: pointer;
            top: 0; left: 0; right: 0; bottom: 0;
            background-color: var(--medium-gray);
            transition: .4s;
            border-radius: 34px;
        }
        .slider:before {
            position: absolute;
            content: "";
            height: 16px; width: 16px;
            left: 4px; bottom: 4px;
            background-color: white;
            transition: .4s;
            border-radius: 50%;
        }
        input:checked + .slider { background-color: var(--rapidapi-blue); }
        input:checked + .slider:before { transform: translateX(20px); }

        .sort-button {
            padding: 0.5rem 1rem;
            background-color: var(--white);
            border: 1px solid var(--medium-gray);
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        .sort-button:hover { background-color: var(--light-gray); }

        /* --- API Grid --- */
        .api-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }

        /* --- API Card --- */
        .api-card {
            background-color: var(--white);
            border: 1px solid var(--medium-gray);
            border-radius: 12px;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            transition: box-shadow 0.3s, transform 0.3s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .api-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        }
        .api-card.is-premium {
            border: 2px solid var(--premium-gold);
            box-shadow: 0 0 15px rgba(255, 215, 0, 0.4);
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 0.75rem;
        }
        .api-name {
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--rapidapi-blue);
        }
        .api-pricing {
            font-size: 0.9rem;
            font-weight: 500;
            color: var(--text-light);
            background: var(--light-gray);
            padding: 0.25rem 0.5rem;
            border-radius: 6px;
        }
        .api-description {
            font-size: 0.95rem;
            color: var(--dark-gray);
            margin-bottom: 1rem;
            flex-grow: 1;
        }
        
        /* Badges Section */
        .badges-section {
            border-top: 1px solid var(--medium-gray);
            padding-top: 1rem;
            margin-top: auto;
        }
        .badges-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }
        .badges-title {
            font-weight: 600;
            font-size: 1rem;
        }
        .badge-counter {
            font-size: 0.9rem;
            color: var(--text-light);
            font-weight: 500;
        }
        .badges-container {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .badge {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.75rem;
            border-radius: 16px;
            font-size: 0.8rem;
            font-weight: 500;
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: default;
        }
        .badge:hover {
            transform: scale(1.05);
            box-shadow: 0 2px 5px rgba(0,0,0,0.15);
        }
        .badge i { margin-right: 6px; }

        /* Individual Badge Styles */
        .badge.badge-trusted { background-color: var(--badge-trusted-bg); color: var(--badge-trusted-text); }
        .badge.badge-fast { background-color: var(--badge-fast-bg); color: var(--badge-fast-text); }
        .badge.badge-blazing { background-color: var(--badge-blazing-bg); color: var(--badge-blazing-text); }
        .badge.badge-enterprise { background-color: var(--badge-enterprise-bg); color: var(--badge-enterprise-text); }
        .badge.badge-community { background-color: var(--badge-community-bg); color: var(--badge-community-text); }
        .badge.badge-downtime { background: var(--badge-downtime-bg); color: var(--badge-downtime-text); }
        .badge.badge-security { background-color: var(--badge-security-bg); color: var(--badge-security-text); }
        .badge.badge-volume { background-color: var(--badge-volume-bg); color: var(--badge-volume-text); }

        /* "Wow" Factors */
        .revenue-indicator {
            display: inline-block;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--premium-revenue-color);
            background-color: rgba(13, 135, 75, 0.1);
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            margin-top: 4px;
        }
        .trust-score {
            margin-top: 1rem;
        }
        .trust-score-label {
            font-size: 0.8rem;
            font-weight: 500;
            color: var(--text-light);
            margin-bottom: 0.25rem;
            display: flex;
            justify-content: space-between;
        }
        .progress-bar-container {
            width: 100%;
            height: 8px;
            background-color: var(--medium-gray);
            border-radius: 4px;
            overflow: hidden;
        }
        .progress-bar {
            height: 100%;
            background-color: var(--rapidapi-blue);
            border-radius: 4px;
            transition: width 0.5s ease-in-out;
        }
        
        /* --- Tooltip --- */
        .tooltip {
            position: fixed;
            background-color: #333;
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.2s;
            z-index: 1200;
            pointer-events: none;
            max-width: 250px;
        }

        .no-results {
            text-align: center;
            padding: 3rem;
            color: var(--text-light);
        }

        /* --- Desktop & Tablet Media Queries --- */
        @media (min-width: 768px) {
            .mobile-menu-toggle, .sidebar-close-btn { display: none; }
            .sidebar {
                position: sticky;
                top: 0; /* Align with bottom of header */
                height: 100vh;
                transform: translateX(0);
                flex-shrink: 0;
                padding-top: 70px; /* Space for fixed header */
            }
            .poc-container {
                flex-direction: row;
            }
            .main-content {
                padding: 1.5rem 2rem;
            }
            .main-wrapper {
                flex-direction: column;
                flex-grow: 1;
            }
            .header {
                position: sticky;
                top: 0;
                width: 100%;
            }
            .api-grid {
                grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            }
            .controls-wrapper {
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
            }
        }
    </style>
</head>
<body>

    <div class="main-wrapper">
        <header class="header">
            <a href="#" class="header-logo"><i class="fa-solid fa-bolt"></i> RapidAPI</a>
            <button class="mobile-menu-toggle" id="mobile-menu-toggle" aria-label="Ouvrir le menu">
                <i class="fa-solid fa-bars"></i>
            </button>
        </header>

        <div class="poc-container">
            <aside class="sidebar" id="sidebar">
                <button class="sidebar-close-btn" id="sidebar-close-btn" aria-label="Fermer le menu">&times;</button>

                <div class="sidebar-section">
                    <h3 class="sidebar-title">Catégories</h3>
                    <ul class="filter-list">
                        <li class="filter-item"><a href="#">Données</a></li>
                        <li class="filter-item"><a href="#">Finance</a></li>
                        <li class="filter-item"><a href="#">Sports</a></li>
                        <li class="filter-item"><a href="#">Météo</a></li>
                        <li class="filter-item"><a href="#">Traduction</a></li>
                    </ul>
                </div>

                <div class="sidebar-section">
                    <h3 class="sidebar-title">Filtrer par Badges</h3>
                    <ul class="filter-list" id="badge-filters">
                        </ul>
                </div>
            </aside>

            <main class="main-content">
                <div class="content-header">
                    <div class="search-bar-wrapper">
                        <i class="fa-solid fa-search"></i>
                        <input type="text" id="search-input" placeholder="Rechercher une API...">
                    </div>
                    <div class="controls-wrapper">
                        <div class="toggle-switch">
                            <label class="switch">
                                <input type="checkbox" id="show-badged-only">
                                <span class="slider"></span>
                            </label>
                            <label for="show-badged-only">Afficher uniquement les APIs avec badges</label>
                        </div>
                        <button id="sort-by-badges" class="sort-button">
                            Trier par nombre de badges <i class="fa-solid fa-sort"></i>
                        </button>
                    </div>
                </div>

                <div class="api-grid" id="api-grid">
                    <div class="loader-container">
                        <div class="loader"></div>
                    </div>
                </div>
            </main>
        </div>
    </div>
    
    <div class="tooltip" id="tooltip"></div>

    <script>
    document.addEventListener('DOMContentLoaded', () => {

        // --- SÉLECTEURS DOM ---
        const apiGrid = document.getElementById('api-grid');
        const searchInput = document.getElementById('search-input');
        const showBadgedOnlyToggle = document.getElementById('show-badged-only');
        const sortByBadgesBtn = document.getElementById('sort-by-badges');
        const badgeFiltersContainer = document.getElementById('badge-filters');
        const tooltip = document.getElementById('tooltip');
        const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
        const sidebar = document.getElementById('sidebar');
        const sidebarCloseBtn = document.getElementById('sidebar-close-btn');

        // --- ÉTAT DE L'APPLICATION ---
        let allApis = [];
        let activeBadgeFilters = new Set();
        let sortAsc = false;

        // --- DÉFINITIONS DES BADGES (pour tooltips, icônes, etc.) ---
        const badgeDetails = {
            'trusted_api': { name: 'Trusted API', icon: 'fa-solid fa-circle-check', criteria: 'Uptime garanti supérieur à 99%. Fiabilité éprouvée.', className: 'badge-trusted' },
            'lightning_fast': { name: 'Lightning Fast', icon: 'fa-solid fa-bolt', criteria: 'Temps de réponse moyen inférieur à 100ms.', className: 'badge-fast' },
            'blazing_speed': { name: 'Blazing Speed', icon: 'fa-solid fa-rocket', criteria: 'Performance d\'élite avec un temps de réponse moyen sous les 50ms.', className: 'badge-blazing' },
            'enterprise_ready': { name: 'Enterprise Ready', icon: 'fa-solid fa-shield-halved', criteria: 'Conforme aux standards entreprise avec un uptime de 99.9%+', className: 'badge-enterprise' },
            'community_proven': { name: 'Community Proven', icon: 'fa-solid fa-users', criteria: 'Adoptée et validée par plus de 1000 développeurs actifs.', className: 'badge-community' },
            'zero_downtime': { name: 'Zero Downtime', icon: 'fa-solid fa-gem', criteria: 'Disponibilité exceptionnelle de 99.99%+. Le summum de la fiabilité.', className: 'badge-downtime' },
            'security_certified': { name: 'Security Certified', icon: 'fa-solid fa-lock', criteria: 'Audit de sécurité réussi et certification de conformité (ex: SOC 2).', className: 'badge-security' },
            'high_volume_ready': { name: 'High Volume Ready', icon: 'fa-solid fa-chart-line', criteria: 'Capable de gérer plus de 10,000 requêtes par minute sans dégradation.', className: 'badge-volume' }
        };
        
        const premiumBadges = new Set(['enterprise_ready', 'zero_downtime']);

        // --- FONCTIONS ---

        /**
         * Récupère les données de l'API
         */
        async function fetchApiData() {
            try {
                const response = await fetch('https://api-performance-badge-system.onrender.com/demo-data');
                if (!response.ok) {
                    throw new Error(`Erreur HTTP: ${response.status}`);
                }
                const data = await response.json();
                allApis = data.demo_apis;
                populateBadgeFilters();
                renderApis();
            } catch (error) {
                apiGrid.innerHTML = `<p class="no-results">Impossible de charger les données des APIs. Veuillez réessayer plus tard.</p>`;
                console.error("Erreur lors de la récupération des données:", error);
            }
        }

        /**
         * Crée et affiche les filtres de badges dans la sidebar
         */
        function populateBadgeFilters() {
            let filterHtml = '';
            for (const key in badgeDetails) {
                const badge = badgeDetails[key];
                filterHtml += `
                    <li class="filter-item">
                        <a data-badge-key="${key}">
                            <span class="badge-filter-icon ${badge.className}"><i class="${badge.icon}"></i></span>
                            ${badge.name}
                        </a>
                    </li>
                `;
            }
            badgeFiltersContainer.innerHTML = filterHtml;
            // Ajout des écouteurs après la création des éléments
            document.querySelectorAll('#badge-filters a').forEach(filter => {
                filter.addEventListener('click', handleBadgeFilterClick);
            });
        }

        /**
         * Gère le clic sur un filtre de badge
         */
        function handleBadgeFilterClick(event) {
            const link = event.currentTarget;
            const badgeKey = link.dataset.badgeKey;
            
            link.classList.toggle('active');
            if (activeBadgeFilters.has(badgeKey)) {
                activeBadgeFilters.delete(badgeKey);
            } else {
                activeBadgeFilters.add(badgeKey);
            }
            renderApis();
        }

        /**
         * Génère le HTML pour une seule carte d'API
         */
        function createApiCardHtml(api) {
            const hasPremiumBadge = api.badges.some(b => premiumBadges.has(b));
            const cardClasses = `api-card ${hasPremiumBadge ? 'is-premium' : ''}`;
            const badgeCount = api.badges.length;
            const trustScore = 20 + (badgeCount * 10); // Calcul simple du score de confiance

            let badgesHtml = '';
            if (badgeCount > 0) {
                badgesHtml = api.badges.map(badgeKey => {
                    const badge = badgeDetails[badgeKey];
                    if (!badge) return '';
                    return `<span class="badge ${badge.className}" data-tooltip="${badge.criteria}">
                                <i class="${badge.icon}"></i> ${badge.name}
                            </span>`;
                }).join('');
            } else {
                badgesHtml = '<p style="color: var(--text-light); font-size: 0.9em;">Cette API n\'a pas encore de badges.</p>';
            }

            return `
                <div class="${cardClasses}">
                    <div class="card-header">
                        <div>
                            <h3 class="api-name">${api.name}</h3>
                            ${hasPremiumBadge ? '<span class="revenue-indicator"><i class="fa-solid fa-arrow-trend-up"></i> Premium Revenue +</span>' : ''}
                        </div>
                        <span class="api-pricing">${api.pricing}</span>
                    </div>
                    <p class="api-description">${api.description}</p>
                    
                    ${hasPremiumBadge ? `
                    <div class="trust-score">
                        <div class="trust-score-label">
                            <span>Score de confiance</span>
                            <span>${trustScore}%</span>
                        </div>
                        <div class="progress-bar-container">
                            <div class="progress-bar" style="width: ${trustScore}%;"></div>
                        </div>
                    </div>
                    ` : ''}

                    <div class="badges-section">
                        <div class="badges-header">
                            <h4 class="badges-title">Badges de Performance</h4>
                            <span class="badge-counter">${badgeCount} badge${badgeCount > 1 ? 's' : ''} gagné${badgeCount > 1 ? 's' : ''}</span>
                        </div>
                        <div class="badges-container">
                            ${badgesHtml}
                        </div>
                    </div>
                </div>
            `;
        }

        /**
         * Affiche les APIs dans la grille après filtrage et tri
         */
        function renderApis() {
            let apisToRender = [...allApis];

            // 1. Filtrage par recherche
            const searchTerm = searchInput.value.toLowerCase();
            if (searchTerm) {
                apisToRender = apisToRender.filter(api => api.name.toLowerCase().includes(searchTerm));
            }

            // 2. Filtrage "badgées uniquement"
            if (showBadgedOnlyToggle.checked) {
                apisToRender = apisToRender.filter(api => api.badges.length > 0);
            }

            // 3. Filtrage par badges sélectionnés
            if (activeBadgeFilters.size > 0) {
                apisToRender = apisToRender.filter(api => 
                    [...activeBadgeFilters].every(filterKey => api.badges.includes(filterKey))
                );
            }

            // Affichage du résultat
            if (apisToRender.length > 0) {
                apiGrid.innerHTML = apisToRender.map(createApiCardHtml).join('');
            } else {
                apiGrid.innerHTML = `<p class="no-results">Aucune API ne correspond à vos critères de recherche.</p>`;
            }
        }
        
        // --- GESTIONNAIRES D'ÉVÉNEMENTS ---

        searchInput.addEventListener('input', renderApis);
        showBadgedOnlyToggle.addEventListener('change', renderApis);

        sortByBadgesBtn.addEventListener('click', () => {
            sortAsc = !sortAsc;
            allApis.sort((a, b) => {
                return sortAsc ? a.badges.length - b.badges.length : b.badges.length - a.badges.length;
            });
            sortByBadgesBtn.querySelector('i').className = sortAsc ? 'fa-solid fa-sort-up' : 'fa-solid fa-sort-down';
            renderApis();
        });

        // Gestion du tooltip (avec délégation d'événement)
        apiGrid.addEventListener('mouseover', event => {
            const target = event.target.closest('.badge[data-tooltip]');
            if (!target) return;
            
            tooltip.textContent = target.dataset.tooltip;
            tooltip.style.opacity = '1';
            tooltip.style.visibility = 'visible';
            
            const rect = target.getBoundingClientRect();
            tooltip.style.left = `${rect.left + rect.width / 2 - tooltip.offsetWidth / 2}px`;
            tooltip.style.top = `${rect.top - tooltip.offsetHeight - 8}px`;
        });
        
        apiGrid.addEventListener('mouseout', event => {
            const target = event.target.closest('.badge[data-tooltip]');
            if (!target) return;

            tooltip.style.opacity = '0';
            tooltip.style.visibility = 'hidden';
        });
        
        // Gestion Menu Mobile
        mobileMenuToggle.addEventListener('click', () => {
            sidebar.classList.add('is-open');
        });
        
        sidebarCloseBtn.addEventListener('click', () => {
            sidebar.classList.remove('is-open');
        });

        // --- INITIALISATION ---
        fetchApiData();
    });
    </script>
</body>
</html>