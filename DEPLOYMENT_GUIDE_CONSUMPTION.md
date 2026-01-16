# Deployment Guide - Consumption Pricing Calculator

## Quick Deploy to Streamlit Cloud (15 minutes)

### Step 1: GitHub Setup

1. Create new repository: `ai-platform-pricing-calculator`
2. Upload files:
   - `consumption_pricing_calculator.py`
   - `requirements_consumption.txt` → rename to `requirements.txt`
   - `README_CONSUMPTION.md` → rename to `README.md`

### Step 2: Streamlit Cloud Deploy

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select repository: `ai-platform-pricing-calculator`
5. Main file: `consumption_pricing_calculator.py`
6. Deploy!

### Step 3: Share with Prospects

Your URL: `https://[your-app-name].streamlit.app`

**Use in sales:**
- Screen share during discovery calls
- Include in follow-up emails
- Reference in proposals
- Let buyers self-serve pricing estimates

---

## Local Testing First (Recommended)

```bash
# Install dependencies
pip install -r requirements_consumption.txt

# Run locally
streamlit run consumption_pricing_calculator.py

# Test all features:
# ✓ Size templates work
# ✓ Build & run phases calculate correctly
# ✓ Deployment comparison displays
# ✓ Multi-year projections render
# ✓ Exports download properly
```

---

## Customization Before Deploy

### 1. Update Default Platform Fee

```python
# In sidebar section
platform_fee = st.number_input(
    "Annual Platform Fee ($)",
    value=150000,  # ← Change this to your typical deal size
    ...
)
```

### 2. Adjust Size Templates

```python
SIZE_TEMPLATES = {
    'Small': {
        'annual_queries': 125000,  # ← Adjust to your customer profiles
        ...
    }
}
```

### 3. Modify Deployment Options

```python
DEPLOYMENT_MODELS = {
    'Customer VPC': {
        'queries_per_credit': 400,  # ← Adjust efficiency ratios
        ...
    }
}
```

---

## Professional Presentation Tips

### During Sales Calls

**Opening:**
"I've built an interactive pricing calculator so you can see exactly how costs work. Let me share my screen..."

**Walk Through:**
1. Show size templates → "Most customers like you fall in the Medium category"
2. Explain deployment → "Customer VPC offers 4x better efficiency"
3. Model growth → "If you grow 20% per year, here's your 3-year path"
4. Export summary → "I'll email you these numbers for internal review"

**Closing:**
"I can send you the calculator link so your finance team can adjust assumptions directly."

### In Proposals

**Include:**
- Calculator link (for interactive exploration)
- Executive summary export (for printed materials)
- CSV export (for detailed financial modeling)

**Reference in SOW:**
"Pricing based on estimates from [calculator URL] using the following assumptions:
- Annual Query Volume: 200,000
- Deployment: Customer VPC
- Queries per Credit: 400
- Platform Fee: $150,000/year"

---

## Maintenance

### Update Exchange Rates

If credit economics change:

```python
credit_cost = st.number_input(
    "Cost per Credit ($)",
    value=5,  # ← Update this value
    ...
)
```

Commit and push to GitHub → Streamlit auto-redeploys.

### Add New Deployment Options

Add to `DEPLOYMENT_MODELS` dictionary:

```python
'Hybrid VPC': {
    'queries_per_credit': 250,
    'description': 'Split deployment model',
    'benefits': ['Balanced cost/control'],
    'considerations': ['Requires coordination']
}
```

### Seasonal Updates

Review quarterly:
- Size template volumes (based on actual customer data)
- Default platform fee (based on average ASP)
- Growth rate defaults (based on renewal data)

---

## Troubleshooting

### "App won't load"
- Check Python syntax in code
- Verify all imports are in requirements.txt
- View logs in Streamlit Cloud dashboard

### "Charts not rendering"
- Ensure plotly version matches requirements
- Clear browser cache
- Try different browser

### "Numbers look wrong"
- Verify credit_cost and queries_per_credit values
- Check calculation logic in calculate_costs()
- Test with known examples (e.g., 200K queries should need 500 credits at 400 queries/credit)

---

## Analytics (Optional)

Want to track calculator usage?

Add to code:
```python
import streamlit as st

# Track calculation events
if st.button("Calculate"):
    st.session_state.calculations += 1
    # Log to your analytics platform
```

---

## Security & Privacy

**Data Privacy:**
- No user inputs are stored
- Each session is isolated
- Calculator runs client-side in browser

**Making Private:**
- Free tier = public access
- Paid tier = authentication & access control
- Enterprise tier = SSO and private deployment

---

## Success Metrics

Track impact:
- **Sales velocity**: Time from demo to proposal (should decrease)
- **Win rate**: Deals where calculator used vs. not used
- **Deal size**: Average ASP where pricing was transparent
- **Objection rate**: "Too expensive" objections (should decrease)

---

## Next Steps

1. ✅ Test locally
2. ✅ Deploy to Streamlit
3. ✅ Customize defaults for your business
4. ✅ Train sales team on usage
5. ✅ Include in sales playbook
6. ✅ Reference in proposals
7. ✅ Iterate based on feedback

**You now have a competitive differentiator for pricing transparency.** 🚀
