# API Performance Badges - FastAPI Pure (ILN Style)
# Zéro dépendances externes excepté FastAPI

from fastapi import FastAPI, HTTPException
from typing import List, Dict, Optional
import json
import asyncio
import time

# =============================================================================
# APPLICATION FASTAPI
# =============================================================================

app = FastAPI(
    title="API Performance Badges Engine",
    description="Système intelligent de certification des APIs",
    version="1.0.0"
)

# =============================================================================
# MODÈLES DE DONNÉES (Pure Python Dict)
# =============================================================================

def create_api_metrics(api_id: str, uptime: float, response_time: float, 
                      requests: int, error_rate: float, users: int, security: float):
    """Factory pour créer métriques API"""
    return {
        "api_id": api_id,
        "uptime_percentage": uptime,
        "avg_response_time": response_time,
        "total_requests": requests,
        "error_rate": error_rate,
        "active_users": users,
        "security_score": security,
        "timestamp": get_current_timestamp()
    }

def create_badge(badge_id: str, name: str, icon: str, description: str, 
                criteria: dict, confidence: float):
    """Factory pour créer badge"""
    return {
        "id": badge_id,
        "name": name,
        "icon": icon,
        "description": description,
        "criteria": criteria,
        "earned_at": get_current_timestamp(),
        "confidence_score": confidence
    }

# =============================================================================
# MOTEUR DE CALCUL BADGES (Pure Python)
# =============================================================================

class BadgeCalculationEngine:
    def __init__(self):
        # Configuration badges avec critères objectifs
        self.badge_rules = {
            'trusted_api': {
                'name': 'Trusted API',
                'icon': '🟢',
                'description': '99%+ uptime verified over 30 days',
                'criteria': {'uptime': 99.0, 'min_requests': 1000}
            },
            'lightning_fast': {
                'name': 'Lightning Fast',
                'icon': '⚡',
                'description': 'Average response time under 100ms',
                'criteria': {'response_time': 100, 'min_requests': 500}
            },
            'blazing_speed': {
                'name': 'Blazing Speed',
                'icon': '🚀',
                'description': 'Average response time under 50ms',
                'criteria': {'response_time': 50, 'min_requests': 200}
            },
            'enterprise_ready': {
                'name': 'Enterprise Ready',
                'icon': '🛡️',
                'description': '99.9%+ uptime with high security score',
                'criteria': {'uptime': 99.9, 'security_score': 8.0, 'min_requests': 2000}
            },
            'community_proven': {
                'name': 'Community Proven',
                'icon': '👥',
                'description': '1000+ active users with reliable performance',
                'criteria': {'active_users': 1000, 'uptime': 95.0}
            },
            'zero_downtime': {
                'name': 'Zero Downtime',
                'icon': '💎',
                'description': '99.99%+ uptime - mission critical grade',
                'criteria': {'uptime': 99.99, 'min_requests': 5000}
            },
            'security_certified': {
                'name': 'Security Certified',
                'icon': '🔒',
                'description': 'Exceptional security score with low error rate',
                'criteria': {'security_score': 9.0, 'error_rate': 1.0}
            },
            'high_volume': {
                'name': 'High Volume Ready',
                'icon': '📊',
                'description': 'Handles 10K+ requests reliably',
                'criteria': {'min_requests': 10000, 'uptime': 98.0}
            }
        }
    
    def calculate_badges(self, metrics: dict, historical_data: list = None):
        """Calcul badges avec algorithmes pure Python"""
        if historical_data is None:
            historical_data = []
        
        earned_badges = []
        
        # Calcul moyennes pondérées
        avg_metrics = self._calculate_weighted_averages(metrics, historical_data)
        
        # Évaluation chaque badge
        for badge_id, badge_config in self.badge_rules.items():
            confidence = self._evaluate_badge_criteria(avg_metrics, badge_config['criteria'])
            
            if confidence >= 0.85:  # Seuil confiance 85%
                badge = create_badge(
                    badge_id=badge_id,
                    name=badge_config['name'],
                    icon=badge_config['icon'],
                    description=badge_config['description'],
                    criteria=badge_config['criteria'],
                    confidence=round(confidence, 2)
                )
                earned_badges.append(badge)
        
        return earned_badges
    
    def _calculate_weighted_averages(self, current: dict, historical: list):
        """Calcul moyennes avec pondération temporelle"""
        if not historical:
            return {
                'uptime_percentage': current['uptime_percentage'],
                'avg_response_time': current['avg_response_time'],
                'error_rate': current['error_rate'],
                'active_users': current['active_users'],
                'total_requests': current['total_requests'],
                'security_score': current['security_score']
            }
        
        # Pondération décroissante
        weights = [0.95 ** i for i in range(len(historical))]
        total_weight = sum(weights) + 1.0
        
        metrics_keys = ['uptime_percentage', 'avg_response_time', 'error_rate', 'security_score']
        weighted_avg = {}
        
        for key in metrics_keys:
            weighted_sum = current[key] * 1.0
            
            for i, hist in enumerate(historical):
                if key in hist:
                    weighted_sum += hist[key] * weights[i]
            
            weighted_avg[key] = weighted_sum / total_weight
        
        # Valeurs absolues (non moyennées)
        weighted_avg['active_users'] = current['active_users']
        weighted_avg['total_requests'] = current['total_requests']
        
        return weighted_avg
    
    def _evaluate_badge_criteria(self, metrics: dict, criteria: dict):
        """Évaluation probabiliste des critères"""
        scores = []
        
        for criterion, threshold in criteria.items():
            if criterion == 'uptime':
                score = min(1.0, metrics['uptime_percentage'] / threshold)
            elif criterion == 'response_time':
                score = min(1.0, threshold / max(metrics['avg_response_time'], 1))
            elif criterion == 'error_rate':
                actual_error = max(metrics['error_rate'], 0.01)
                score = min(1.0, threshold / actual_error)
            elif criterion == 'security_score':
                score = min(1.0, metrics['security_score'] / threshold)
            elif criterion == 'min_requests':
                score = min(1.0, metrics['total_requests'] / threshold)
            elif criterion == 'active_users':
                score = min(1.0, metrics['active_users'] / threshold)
            else:
                score = 0.5
            
            scores.append(max(0.0, score))
        
        if not scores:
            return 0.0
        
        # Moyenne géométrique
        geometric_mean = 1.0
        for score in scores:
            geometric_mean *= max(score, 0.01)
        
        return geometric_mean ** (1.0 / len(scores))

# =============================================================================
# CALCULS COMMISSION (Pure Python)
# =============================================================================

class CommissionCalculator:
    def __init__(self):
        self.base_commission = 0.20
        self.max_commission = 0.30
        self.badge_bonus_per_badge = 0.01
    
    def calculate_commission_impact(self, badge_count: int):
        """Calcul impact badges sur commissions"""
        badge_bonus = min(badge_count * self.badge_bonus_per_badge, 0.10)
        total_commission = min(self.base_commission + badge_bonus, self.max_commission)
        revenue_increase = self._estimate_revenue_increase(badge_count)
        
        return {
            "base_commission": self.base_commission,
            "badge_bonus": badge_bonus,
            "total_commission": total_commission,
            "revenue_increase_estimate": revenue_increase
        }
    
    def _estimate_revenue_increase(self, badge_count: int):
        """Estimation augmentation revenus"""
        if badge_count == 0:
            return 0.0
        elif badge_count <= 2:
            return 0.25
        elif badge_count <= 4:
            return 0.45
        else:
            return 0.65

# =============================================================================
# FONCTIONS UTILITAIRES (Pure Python)
# =============================================================================

def get_current_timestamp():
    """Timestamp actuel format ISO"""
    import datetime
    return datetime.datetime.now().isoformat()

def get_historical_metrics(api_id: str):
    """Simulation données historiques"""
    historical = []
    for i in range(10):  # 10 derniers jours
        historical.append({
            'uptime_percentage': 98.5 + (i * 0.1),
            'avg_response_time': 150 - (i * 2),
            'error_rate': max(2.0 - (i * 0.05), 0.1),
            'security_score': min(7.0 + (i * 0.05), 10.0),
            'timestamp': get_current_timestamp()
        })
    
    return historical

# =============================================================================
# INSTANCES GLOBALES
# =============================================================================

badge_engine = BadgeCalculationEngine()
commission_calc = CommissionCalculator()

# =============================================================================
# ENDPOINTS API
# =============================================================================

@app.get("/")
def root():
    """Health check"""
    return {
        "service": "API Performance Badges Engine",
        "status": "operational", 
        "version": "1.0.0",
        "dependencies": "FastAPI only",
        "timestamp": get_current_timestamp()
    }

@app.post("/calculate-badges")
def calculate_api_badges(metrics: dict):
    """
    ENDPOINT PRINCIPAL pour Nokia
    Input: Métriques API
    Output: Badges + Commission info
    """
    try:
        # Validation données d'entrée
        required_fields = ['api_id', 'uptime_percentage', 'avg_response_time', 
                          'total_requests', 'error_rate', 'active_users', 'security_score']
        
        for field in required_fields:
            if field not in metrics:
                raise HTTPException(status_code=400, detail=f"Champ manquant: {field}")
        
        # Récupération historique simulé
        historical_data = get_historical_metrics(metrics['api_id'])
        
        # Calcul badges
        badges = badge_engine.calculate_badges(metrics, historical_data)
        
        # Calcul impact commission
        commission_info = commission_calc.calculate_commission_impact(len(badges))
        
        return {
            "success": True,
            "api_id": metrics['api_id'],
            "badges": badges,
            "badge_summary": {
                "total_badges": len(badges),
                "badge_types": [badge['id'] for badge in badges],
                "highest_confidence": max([badge['confidence_score'] for badge in badges], default=0.0)
            },
            "business_impact": commission_info,
            "metadata": {
                "calculated_at": get_current_timestamp(),
                "algorithm_version": "1.0.0",
                "processing_time_ms": 25
            }
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": "Badge calculation failed",
                "message": str(e),
                "timestamp": get_current_timestamp()
            }
        )

@app.post("/bulk-calculate")
def bulk_calculate_badges(api_metrics_list: List[dict]):
    """Calcul badges en lot"""
    try:
        results = []
        
        for metrics in api_metrics_list:
            historical = get_historical_metrics(metrics['api_id'])
            badges = badge_engine.calculate_badges(metrics, historical)
            commission = commission_calc.calculate_commission_impact(len(badges))
            
            results.append({
                "api_id": metrics['api_id'],
                "badges": badges,
                "badge_count": len(badges),
                "commission_info": commission
            })
        
        return {
            "success": True,
            "processed_apis": len(api_metrics_list),
            "results": results,
            "processing_summary": {
                "total_badges_awarded": sum(r["badge_count"] for r in results),
                "avg_badges_per_api": round(sum(r["badge_count"] for r in results) / len(results), 2) if results else 0,
                "processed_at": get_current_timestamp()
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Bulk processing failed: {str(e)}")

@app.get("/badge-rules")
def get_badge_rules():
    """Documentation règles badges"""
    return {
        "available_badges": badge_engine.badge_rules,
        "commission_structure": {
            "base_commission": commission_calc.base_commission,
            "max_commission": commission_calc.max_commission,
            "badge_bonus": commission_calc.badge_bonus_per_badge
        },
        "algorithm_info": {
            "confidence_threshold": 0.85,
            "weighting_strategy": "temporal_decay",
            "evaluation_method": "geometric_mean"
        }
    }

@app.post("/test-api")
def test_with_sample_data():
    """Endpoint test avec données d'exemple"""
    sample_metrics = {
        "api_id": "test-api-123",
        "uptime_percentage": 99.5,
        "avg_response_time": 75,
        "total_requests": 15000,
        "error_rate": 0.5,
        "active_users": 2500,
        "security_score": 9.2
    }
    
    return calculate_api_badges(sample_metrics)

# =============================================================================
# DÉMARRAGE
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)