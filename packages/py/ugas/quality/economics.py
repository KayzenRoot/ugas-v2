from __future__ import annotations
from typing import Sequence
from .contracts import RouteEconomics

def failure_adjusted_cost(route:RouteEconomics)->float:
    if not 0<=route.expected_failure_probability<1: raise ValueError("failure probability must be in [0,1)")
    return (route.generation_cost+route.expected_repair_cost)/(1-route.expected_failure_probability)

def choose_route(routes:Sequence[RouteEconomics],*,max_cost:float,max_latency_ms:int)->RouteEconomics:
    eligible=[r for r in routes if failure_adjusted_cost(r)<=max_cost and r.expected_latency_ms<=max_latency_ms]
    if not eligible: raise ValueError("no route satisfies cost/latency envelope")
    return min(eligible,key=lambda r:(failure_adjusted_cost(r),r.expected_latency_ms,r.route_id))

# CODEX-TASK[M21-QUALITY-CONSTRAINED-ROUTING]
# Integrate M19 predicted quality floor and M02 hardware envelope before economics. Cheapest route is
# eligible only if hard quality/security/rights constraints remain satisfied. Track measured vs predicted.
