# AI Platform - Consumption-Based Pricing Calculator

## Overview

CFO-grade pricing transparency tool for consumption-based AI platform pricing. Helps buyers understand total cost of ownership across deployment models, usage phases, and multi-year horizons.

## Core Pricing Model

### Platform Components

**1. Fixed Platform Fee**
- Annual recurring fee for platform access
- Fully editable by user
- No credits included (purely access)
- Flat enterprise fee (no tiers)

**2. Consumption Credits**
- $5 per credit (configurable)
- Credits are required for queries
- Purchased in blocks (minimum 1-year contract)
- No expiration within contract term

**3. Deployment Model Impact**
Query efficiency varies dramatically by deployment:

| Deployment | Queries/Credit | Efficiency |
|------------|---------------|------------|
| **Customer VPC** | 400 | 4x better |
| **Uniphore VPC** | 100 | Baseline |

**This 4x efficiency difference is the critical cost driver.**

### Total Cost Formula

```
Annual Cost = Platform Fee + (Total Queries ÷ Queries per Credit × $5)
Cost per Query = Annual Cost ÷ Total Queries
```

## Key Features

### 1. **Three Volume Estimation Methods**

**Size Templates:**
- Small: 125,000 queries/year (pilot/small team)
- Medium: 200,000 queries/year (department-level)
- Large: 300,000 queries/year (enterprise-wide)
- Custom: Define your own volume

**Build & Run Phases:**
- Separate estimation for development vs. production
- Build Phase: Higher intensity, shorter duration (testing, tuning, pilot)
- Run Phase: Steady-state production operations
- Customizable duration and query rates for each phase

**Direct Input:**
- Enter known annual query volume directly
- Best for customers with existing analytics

### 2. **Deployment Model Comparison**

Side-by-side analysis showing:
- Total annual cost for each deployment
- Cost per query breakdown
- Credits required
- Benefits and considerations
- Savings opportunity

**Decision Support:**
- Identifies cheaper deployment option
- Calculates cost difference ($) and percentage
- Highlights efficiency advantages
- Shows trade-offs (cost vs. control vs. speed)

### 3. **Multi-Year Projection**

- 1-5 year cost modeling
- Configurable annual growth rate (0-50%)
- Year-over-year cost and volume trends
- Total Cost of Ownership (TCO) calculation
- Cost per query evolution analysis

### 4. **Cost Transparency Visualizations**

**Cost Composition:**
- Pie chart showing Platform vs. Consumption split
- Detailed breakdown table with all calculations

**Multi-Year Projection:**
- Stacked bar chart: Platform + Consumption by year
- Query volume trend overlay
- Cost per query trend line

**Deployment Comparison:**
- Side-by-side cost cards with metrics
- Stacked bar comparison chart
- Savings calculation and recommendation

### 5. **Executive-Ready Outputs**

**CSV Export:**
- Full multi-year cost breakdown
- All metrics and assumptions
- Ready for Excel modeling

**Executive Summary (TXT):**
- One-page summary with key numbers
- Configuration details
- Deployment comparison
- Multi-year TCO
- Recommendation

## Using the Calculator

### Step 1: Configure Platform Settings (Sidebar)

**Platform Configuration:**
- Set annual platform fee (default: $150,000)
- Set cost per credit (default: $5)

**Deployment Model:**
- Select Customer VPC or Uniphore VPC
- Review deployment description and trade-offs
- Optional: Customize queries/credit ratio

**Volume Estimation Method:**
- Choose: Size Template, Build & Run Phases, or Direct Input

### Step 2: Estimate Query Volume

**If using Size Templates:**
- Click Small/Medium/Large/Custom button
- Review typical profile description
- For Custom, enter specific volume

**If using Build & Run Phases:**
- Set Build Phase: Duration (months) + Queries/month
- Set Run Phase: Duration (months) + Queries/month
- Calculator sums to annual total
- Use for first-year planning when production volume is uncertain

**If using Direct Input:**
- Enter total annual query volume directly
- Best when you have historical usage data

### Step 3: Configure Multi-Year Projection

- Set projection period (1-5 years)
- Set annual growth rate (0-50%)
- Growth compounds year-over-year

### Step 4: Analyze Results

**Year 1 Cost Summary:**
- Total Annual Cost
- Cost per Query
- Monthly Cost
- Credits Needed

**Cost Breakdown:**
- Visual: Platform vs. Consumption pie chart
- Table: Detailed calculation showing all components

**Multi-Year Projection:**
- Chart: Costs and volume by year
- Chart: Cost per query trend
- Table: Year-by-year summary with all metrics
- Summary: Total TCO, total queries, average cost/query

**Deployment Comparison:**
- Side-by-side cards: Customer VPC vs. Uniphore VPC
- Cost difference and percentage savings
- Efficiency analysis
- Benefits and considerations for each option
- Visual: Stacked bar comparison

**Export:**
- Download CSV: Full dataset for analysis
- Download summary: Executive one-pager

## Key Insights and Use Cases

### For Buyers

**Question: "What will this cost us?"**
Answer: Use size template or build/run phases to estimate, see Year 1 cost summary.

**Question: "Should we deploy in our VPC or yours?"**
Answer: Deployment comparison shows exact cost difference and trade-offs.

**Question: "How does cost scale as we grow?"**
Answer: Multi-year projection with growth rate shows TCO and cost per query evolution.

**Question: "What's driving our cost?"**
Answer: Cost composition pie shows platform vs. consumption split.

**Question: "What if our volume is wrong?"**
Answer: Adjust inputs in real-time, instantly see impact on all metrics.

### For Sellers

**Objection: "Your pricing is too expensive"**
Response: Show deployment comparison—Customer VPC offers 4x better efficiency.

**Objection: "We don't know our volume yet"**
Response: Use build & run phases to model realistic ramp-up.

**Objection: "What about year 2 and beyond?"**
Response: Multi-year projection shows predictable costs with growth.

**Need: Proposal cost section**
Response: Export CSV and executive summary for appendix.

**Need: Compare to competitor**
Response: Adjust platform fee and queries/credit to model alternatives.

## Understanding the Numbers

### Cost per Query

**What it means:**
Total cost divided by query volume. The unit economics metric buyers care about.

**Why it matters:**
- Enables apples-to-apples comparison across vendors
- Shows economies of scale (should decrease as volume grows)
- Directly comparable to current costs (if replacing existing system)

**Typical ranges:**
- Customer VPC: $0.03-0.08 per query (high efficiency)
- Uniphore VPC: $0.10-0.25 per query (managed convenience)

### Credits Required

**What it means:**
Number of consumption credits needed for estimated query volume.

**Why it matters:**
- Determines consumption spend (Credits × $5)
- Drives budget planning and procurement
- Must be purchased in blocks (annual contract)

**Formula:**
```
Credits = Total Queries ÷ Queries per Credit
```

### Platform vs. Consumption Split

**What it means:**
Percentage of total cost that's fixed (platform) vs. variable (consumption).

**Why it matters:**
- High platform %: Fixed costs dominate, volume doesn't matter much
- High consumption %: Variable costs dominate, efficiency critical
- Sweet spot: ~40% platform / 60% consumption for predictable scaling

**How deployment affects it:**
- Customer VPC: Higher consumption % (efficiency makes credits go further)
- Uniphore VPC: Platform becomes larger % of total (credits consumed faster)

## Business Scenarios

### Scenario 1: Pilot to Production

**Challenge:** Buyer wants to pilot before committing to enterprise scale.

**Solution:** Use Build & Run Phases
- Build: 3 months × 10,000 queries/month = 30,000 queries
- Run: 9 months × 5,000 queries/month = 45,000 queries
- Year 1 Total: 75,000 queries
- Set growth rate to 100% for Year 2 (full production)
- Show Year 3 at 150,000 queries (sustained growth)

**Outcome:** Buyer sees realistic pilot costs + production ramp.

### Scenario 2: VPC Decision

**Challenge:** CTO wants Customer VPC for control, CFO wants Uniphore VPC for simplicity.

**Solution:** Show deployment comparison
- At 200,000 queries, Customer VPC saves ~$60,000/year
- Show TCO over 3 years: $180,000 difference
- Frame trade-off: Invest in VPC setup, save $180K over contract

**Outcome:** CFO has financial case for CTO's preferred architecture.

### Scenario 3: Volume Uncertainty

**Challenge:** Buyer doesn't know their query volume yet.

**Solution:** Model three scenarios
- Conservative: 125,000 queries (Small template)
- Realistic: 200,000 queries (Medium template)
- Aggressive: 300,000 queries (Large template)
- Export all three scenarios side-by-side

**Outcome:** Buyer sees cost range and can bracket their risk.

### Scenario 4: Competitive Comparison

**Challenge:** Buyer evaluating multiple vendors with different pricing models.

**Solution:** Normalize to cost per query
- Competitor A: Fixed fee $200K (unlimited queries)
- Your model: $150K + consumption
- Find break-even: At what volume are you cheaper?
- Customer VPC: Cheaper above ~125K queries
- Uniphore VPC: Cheaper above ~200K queries

**Outcome:** Clear decision criteria based on estimated volume.

## Customization Guide

### Adjusting Deployment Models

To add new deployment options or adjust efficiency:

```python
DEPLOYMENT_MODELS = {
    'Customer VPC': {
        'queries_per_credit': 400,  # Change this value
        'description': 'Deploy in your own Virtual Private Cloud',
        'benefits': ['4x query efficiency', 'Full data control'],
        'considerations': ['Infrastructure management']
    },
    # Add new models here
}
```

### Changing Size Templates

To adjust customer size definitions:

```python
SIZE_TEMPLATES = {
    'Small': {
        'annual_queries': 125000,  # Adjust volume
        'description': 'Small team or pilot',
        'typical_profile': '10-25 users'
    },
    # Modify or add templates
}
```

### Adjusting Credit Economics

To change credit pricing or default values:

```python
# In sidebar
credit_cost = st.number_input(
    "Cost per Credit ($)",
    value=5,  # Change default here
    ...
)
```

### Adding Industry Benchmarks

To include industry-specific query patterns:

```python
INDUSTRY_PATTERNS = {
    'Customer Service': {
        'queries_per_agent_per_day': 50,
        'description': 'Contact center usage'
    },
    'Sales': {
        'queries_per_rep_per_day': 30,
        'description': 'Sales team enablement'
    }
}
```

Then create UI for users to input agent count instead of raw queries.

## Technical Details

### Technologies
- **Streamlit**: Interactive web framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive charts

### File Structure
```
consumption_pricing_calculator.py    # Main application
requirements_consumption.txt         # Dependencies
README_CONSUMPTION.md               # This file
```

### Running Locally

```bash
# Install dependencies
pip install -r requirements_consumption.txt

# Run application
streamlit run consumption_pricing_calculator.py

# Open browser to http://localhost:8501
```

### Deploying to Streamlit Cloud

1. Push to GitHub repository
2. Connect to Streamlit Cloud (share.streamlit.io)
3. Deploy from repository
4. Share public URL with prospects/customers

## Best Practices

### For Sales Discovery

1. **Start with size template** to establish baseline
2. **Show deployment comparison** to frame VPC decision
3. **Model multi-year** to demonstrate predictable costs
4. **Export summary** for follow-up email

### For Proposals

1. **Use base case assumptions** (documented in export)
2. **Include both deployment options** with recommendation
3. **Show 3-year TCO** to align with contract terms
4. **Provide CSV** for client's financial review

### For Procurement

1. **Export executive summary** for approvers
2. **Highlight cost per query** for unit economics
3. **Show monthly cost** for budget planning
4. **Include growth scenarios** for capacity planning

### For Contract Negotiation

1. **Reference calculator assumptions** in SOW
2. **Tie credits to volume estimates** from tool
3. **Use deployment comparison** to justify architecture
4. **Show TCO** to frame multi-year commitment

## Common Questions

**Q: Can credits be purchased monthly?**
A: Not in this model. Minimum 1-year contract with annual credit commitment.

**Q: Do unused credits roll over?**
A: Not modeled here. Assume credits are valid for contract term.

**Q: What if actual volume exceeds estimate?**
A: Would require additional credit purchase. Not modeled as "overage" pricing.

**Q: Can I change deployment mid-contract?**
A: Possible but complex. Model treats as distinct options.

**Q: How do I handle seasonal spikes?**
A: Average across 12 months. Don't model monthly fluctuations in this tool.

**Q: What if I want to model pilot + production separately?**
A: Use Build & Run phases with distinct volumes and durations.

## Future Enhancements

Possible additions for v2.0:
- [ ] Monthly usage patterns (handle seasonality)
- [ ] Multiple contract term options (1, 2, 3 year pricing)
- [ ] Overage pricing (pay-per-query beyond purchased credits)
- [ ] Volume discount tiers (bulk credit discounts)
- [ ] Credit expiration modeling (monthly vs. annual)
- [ ] Break-even analysis vs. competitor pricing
- [ ] ROI calculator (savings vs. current state)
- [ ] Team-based estimation (queries per user per day)
- [ ] Industry benchmark templates

## Support

For questions or customization requests, contact your Uniphore team.

---

**Built for Buyer Transparency and Informed Decision-Making**
Uniphore Business AI Cloud | Consumption-Based Pricing
