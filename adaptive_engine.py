from typing import Dict, Any
import logging
from revenue_optimizer import RevenueOptimizer
from risk_assessor import RiskAssessor

class AdaptiveEngine:
    def __init__(self, revenue_optimizer: RevenueOptimizer, risk_assessor: RiskAssessor):
        self.revenue_optimizer = revenue_optimizer
        self.risk_assessor = risk_assessor
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def adjust_strategy(self, business_context: Dict[str, Any]) -> Dict[str, Any]:
        try:
            optimal_price = self.revenue_optimizer.calculate_optimal_price(business_context)
            risks = self.risk_assessor.assess_business_risk()
            
            strategy = {
                'price': optimal_price,
                'risks': risks
            }
            return strategy
        except Exception as e:
            self.logger.error(f"Strategy adjustment failed: {str(e)}")
            raise StrategyAdjustmentError("Failed to adjust business strategy")

class StrategyAdjustmentError(Exception):
    pass