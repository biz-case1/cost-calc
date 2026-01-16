import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Platform - Pricing Calculator",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .pricing-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .deployment-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #007bff;
        margin: 10px 0;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .phase-header {
        background-color: #e7f3ff;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #0066cc;
        margin: 15px 0;
    }
    .comparison-winner {
        background-color: #d4edda;
        border-color: #28a745;
    }
    .insight-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 15px 0;
    }
    .cost-breakdown {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Deployment models with queries per credit
DEPLOYMENT_MODELS = {
    'Customer VPC': {
        'queries_per_credit': 400,
        'description': 'Deploy in your own Virtual Private Cloud',
        'benefits': ['4x query efficiency', 'Full data control', 'Lowest cost per query'],
        'considerations': ['Infrastructure management', 'VPC setup required']
    },
    'Uniphore VPC': {
        'queries_per_credit': 100,
        'description': 'Deploy in Uniphore-managed cloud',
        'benefits': ['Fastest time to value', 'Zero infrastructure overhead', 'Managed updates'],
        'considerations': ['Higher consumption cost', 'Shared infrastructure']
    }
}

# Customer size templates
SIZE_TEMPLATES = {
    'Small': {
        'annual_queries': 125000,
        'description': 'Small team or pilot deployment',
        'typical_profile': '10-25 users, single use case'
    },
    'Medium': {
        'annual_queries': 200000,
        'description': 'Department-level deployment',
        'typical_profile': '25-100 users, 2-3 use cases'
    },
    'Large': {
        'annual_queries': 300000,
        'description': 'Enterprise-wide deployment',
        'typical_profile': '100+ users, multiple use cases'
    },
    'Custom': {
        'annual_queries': 0,
        'description': 'Define your own volume',
        'typical_profile': 'Customize based on your needs'
    }
}

def format_number(value, decimals=0, prefix='', suffix=''):
    """Format numbers with commas"""
    if decimals == 0:
        formatted = f"{value:,.0f}"
    else:
        formatted = f"{value:,.{decimals}f}"
    return f"{prefix}{formatted}{suffix}"

def calculate_costs(annual_queries, platform_fee, credit_cost, queries_per_credit, years=3, growth_rate=0):
    """Calculate comprehensive cost breakdown"""
    results = []
    
    for year in range(1, years + 1):
        # Apply growth rate
        year_queries = annual_queries * ((1 + growth_rate) ** (year - 1))
        
        # Credits needed
        credits_needed = year_queries / queries_per_credit
        
        # Consumption cost
        consumption_cost = credits_needed * credit_cost
        
        # Total annual cost
        total_cost = platform_fee + consumption_cost
        
        # Derived metrics
        cost_per_query = total_cost / year_queries
        monthly_cost = total_cost / 12
        
        results.append({
            'year': year,
            'queries': year_queries,
            'credits_needed': credits_needed,
            'platform_fee': platform_fee,
            'consumption_cost': consumption_cost,
            'total_cost': total_cost,
            'cost_per_query': cost_per_query,
            'monthly_cost': monthly_cost
        })
    
    return results

def estimate_queries_from_phases(build_months, build_queries_per_month, run_months, run_queries_per_month):
    """Estimate annual queries from build and run phases"""
    build_total = build_months * build_queries_per_month
    run_total = run_months * run_queries_per_month
    return build_total + run_total

# Sidebar - Configuration
with st.sidebar:
    st.title("💰 Pricing Calculator")
    
    st.markdown("### 🏢 Platform Configuration")
    
    platform_fee = st.number_input(
        "Annual Platform Fee ($)",
        min_value=0,
        max_value=1000000,
        value=150000,
        step=10000,
        format="%d",
        help="Fixed annual access fee"
    )
    
    credit_cost = st.number_input(
        "Cost per Credit ($)",
        min_value=1,
        max_value=100,
        value=5,
        step=1,
        format="%d",
        help="Price of each consumption credit"
    )
    
    st.markdown("---")
    st.markdown("### 🌐 Deployment Model")
    
    deployment_model = st.radio(
        "Select Deployment",
        options=list(DEPLOYMENT_MODELS.keys()),
        help="Deployment location impacts query efficiency"
    )
    
    queries_per_credit = DEPLOYMENT_MODELS[deployment_model]['queries_per_credit']
    
    # Show deployment details
    st.markdown(f"""
        <div class="deployment-card">
        <strong>{deployment_model}</strong><br>
        <span style="font-size: 24px; color: #007bff;">{queries_per_credit} queries/credit</span><br>
        <small>{DEPLOYMENT_MODELS[deployment_model]['description']}</small>
        </div>
    """, unsafe_allow_html=True)
    
    # Option to adjust queries per credit
    if st.checkbox("Customize queries/credit ratio"):
        queries_per_credit = st.number_input(
            "Queries per Credit",
            min_value=50,
            max_value=1000,
            value=queries_per_credit,
            step=50
        )
    
    st.markdown("---")
    st.markdown("### 📊 Volume Estimation Method")
    
    estimation_method = st.radio(
        "How do you want to estimate volume?",
        options=['Size Template', 'Build & Run Phases', 'Direct Input']
    )

# Main content area
st.title("🎯 AI Platform Pricing & Cost Calculator")

# Volume estimation based on selected method
if estimation_method == 'Size Template':
    st.markdown("## 📏 Select Customer Size Template")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Small\n125K queries", use_container_width=True):
            st.session_state.size_selection = 'Small'
    
    with col2:
        if st.button("Medium\n200K queries", use_container_width=True):
            st.session_state.size_selection = 'Medium'
    
    with col3:
        if st.button("Large\n300K queries", use_container_width=True):
            st.session_state.size_selection = 'Large'
    
    with col4:
        if st.button("Custom", use_container_width=True):
            st.session_state.size_selection = 'Custom'
    
    # Initialize session state
    if 'size_selection' not in st.session_state:
        st.session_state.size_selection = 'Medium'
    
    selected_size = st.session_state.size_selection
    
    st.markdown(f"""
        <div class="phase-header">
        <strong>Selected: {selected_size}</strong><br>
        {SIZE_TEMPLATES[selected_size]['description']}<br>
        <small>{SIZE_TEMPLATES[selected_size]['typical_profile']}</small>
        </div>
    """, unsafe_allow_html=True)
    
    if selected_size == 'Custom':
        annual_queries = st.number_input(
            "Annual Query Volume",
            min_value=1000,
            max_value=10000000,
            value=250000,
            step=10000,
            format="%d"
        )
    else:
        annual_queries = SIZE_TEMPLATES[selected_size]['annual_queries']
        st.metric("Annual Query Volume", format_number(annual_queries))

elif estimation_method == 'Build & Run Phases':
    st.markdown("## 🏗️ Build & Run Phase Estimation")
    
    st.markdown("""
        <div class="insight-box">
        <strong>💡 Usage Pattern Guidance</strong><br>
        Most implementations have two distinct phases with different query patterns:
        <ul>
        <li><strong>Build Phase:</strong> Development, testing, model tuning, pilot deployment (higher intensity, shorter duration)</li>
        <li><strong>Run Phase:</strong> Production operations, steady-state usage (sustained volume)</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏗️ Build Phase")
        build_months = st.slider(
            "Build Phase Duration (months)",
            min_value=1,
            max_value=12,
            value=3,
            help="Typical: 2-4 months for development and pilot"
        )
        
        build_queries_per_month = st.number_input(
            "Queries per Month (Build)",
            min_value=1000,
            max_value=1000000,
            value=20000,
            step=1000,
            format="%d",
            help="Higher volume during testing and tuning"
        )
        
        build_total = build_months * build_queries_per_month
        st.metric("Build Phase Total", format_number(build_total))
    
    with col2:
        st.markdown("### 🚀 Run Phase")
        run_months = st.slider(
            "Run Phase Duration (months)",
            min_value=1,
            max_value=12,
            value=9,
            help="Remaining months in year 1"
        )
        
        run_queries_per_month = st.number_input(
            "Queries per Month (Run)",
            min_value=1000,
            max_value=1000000,
            value=15000,
            step=1000,
            format="%d",
            help="Steady-state production volume"
        )
        
        run_total = run_months * run_queries_per_month
        st.metric("Run Phase Total", format_number(run_total))
    
    annual_queries = estimate_queries_from_phases(
        build_months, build_queries_per_month,
        run_months, run_queries_per_month
    )
    
    st.markdown(f"""
        <div class="phase-header">
        <strong>Year 1 Total Estimated Queries:</strong> {format_number(annual_queries)}<br>
        <small>Build: {format_number(build_total)} + Run: {format_number(run_total)}</small>
        </div>
    """, unsafe_allow_html=True)

else:  # Direct Input
    st.markdown("## 🎯 Direct Volume Input")
    
    annual_queries = st.number_input(
        "Annual Query Volume",
        min_value=1000,
        max_value=10000000,
        value=200000,
        step=10000,
        format="%d",
        help="Total queries you expect to process annually"
    )

# Multi-year growth
st.markdown("---")
st.markdown("## 📈 Multi-Year Projection")

col1, col2 = st.columns(2)

with col1:
    projection_years = st.slider(
        "Projection Period (years)",
        min_value=1,
        max_value=5,
        value=3
    )

with col2:
    growth_rate = st.slider(
        "Annual Growth Rate (%)",
        min_value=0,
        max_value=50,
        value=15,
        help="Expected year-over-year query volume growth"
    ) / 100

# Calculate costs for selected deployment
costs = calculate_costs(
    annual_queries,
    platform_fee,
    credit_cost,
    queries_per_credit,
    projection_years,
    growth_rate
)

# Key Metrics Display
st.markdown("## 💎 Year 1 Cost Summary")

col1, col2, col3, col4 = st.columns(4)

year1 = costs[0]

with col1:
    st.metric(
        "Total Annual Cost",
        format_number(year1['total_cost'], prefix='$'),
        help="Platform fee + consumption"
    )

with col2:
    st.metric(
        "Cost per Query",
        format_number(year1['cost_per_query'], decimals=4, prefix='$'),
        help="Total cost divided by query volume"
    )

with col3:
    st.metric(
        "Monthly Cost",
        format_number(year1['monthly_cost'], prefix='$'),
        help="Average monthly cash flow"
    )

with col4:
    st.metric(
        "Credits Needed",
        format_number(year1['credits_needed']),
        help="Total credits for annual volume"
    )

# Cost Breakdown
st.markdown("## 📊 Year 1 Cost Breakdown")

col1, col2 = st.columns(2)

with col1:
    # Cost composition pie chart
    fig_pie = go.Figure(data=[go.Pie(
        labels=['Platform Fee', 'Consumption (Credits)'],
        values=[year1['platform_fee'], year1['consumption_cost']],
        marker=dict(colors=['#667eea', '#764ba2']),
        textinfo='label+percent+value',
        texttemplate='%{label}<br>$%{value:,.0f}<br>(%{percent})',
        hovertemplate='%{label}<br>$%{value:,.0f}<br>%{percent}<extra></extra>'
    )])
    
    fig_pie.update_layout(
        title=f"Cost Composition - {deployment_model}",
        height=400
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    # Cost breakdown details
    st.markdown(f"""
        <div class="cost-breakdown">
        <h4>Detailed Breakdown</h4>
        <table style="width:100%; border-collapse: collapse;">
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;"><strong>Annual Query Volume</strong></td>
            <td style="padding: 8px; text-align: right;">{format_number(year1['queries'])}</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;"><strong>Queries per Credit</strong></td>
            <td style="padding: 8px; text-align: right;">{format_number(queries_per_credit)}</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;"><strong>Credits Required</strong></td>
            <td style="padding: 8px; text-align: right;">{format_number(year1['credits_needed'])}</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;"><strong>Cost per Credit</strong></td>
            <td style="padding: 8px; text-align: right;">${credit_cost}</td>
        </tr>
        <tr style="border-bottom: 2px solid #000;">
            <td style="padding: 8px;"><strong>Consumption Cost</strong></td>
            <td style="padding: 8px; text-align: right;">{format_number(year1['consumption_cost'], prefix='$')}</td>
        </tr>
        <tr style="border-bottom: 1px solid #ddd;">
            <td style="padding: 8px;"><strong>Platform Fee</strong></td>
            <td style="padding: 8px; text-align: right;">{format_number(year1['platform_fee'], prefix='$')}</td>
        </tr>
        <tr style="background-color: #f0f0f0; font-weight: bold;">
            <td style="padding: 8px;"><strong>Total Annual Cost</strong></td>
            <td style="padding: 8px; text-align: right;">{format_number(year1['total_cost'], prefix='$')}</td>
        </tr>
        </table>
        </div>
    """, unsafe_allow_html=True)

# Multi-year projection
if projection_years > 1:
    st.markdown(f"## 📅 {projection_years}-Year Financial Projection")
    
    # Prepare data for charts
    years_list = [f"Year {c['year']}" for c in costs]
    total_costs = [c['total_cost'] for c in costs]
    platform_fees = [c['platform_fee'] for c in costs]
    consumption_costs = [c['consumption_cost'] for c in costs]
    queries_list = [c['queries'] for c in costs]
    cost_per_query_list = [c['cost_per_query'] for c in costs]
    
    # Stacked bar chart for multi-year costs
    fig_multiyear = go.Figure()
    
    fig_multiyear.add_trace(go.Bar(
        name='Platform Fee',
        x=years_list,
        y=platform_fees,
        marker_color='#667eea',
        text=[format_number(v, prefix='$') for v in platform_fees],
        textposition='inside'
    ))
    
    fig_multiyear.add_trace(go.Bar(
        name='Consumption',
        x=years_list,
        y=consumption_costs,
        marker_color='#764ba2',
        text=[format_number(v, prefix='$') for v in consumption_costs],
        textposition='inside'
    ))
    
    fig_multiyear.add_trace(go.Scatter(
        name='Query Volume',
        x=years_list,
        y=queries_list,
        mode='lines+markers+text',
        line=dict(color='#28a745', width=3),
        marker=dict(size=10),
        text=[format_number(v) for v in queries_list],
        textposition='top center',
        yaxis='y2'
    ))
    
    fig_multiyear.update_layout(
        title=f"{projection_years}-Year Cost and Volume Projection (Growth: {growth_rate*100:.0f}%/year)",
        barmode='stack',
        height=500,
        yaxis=dict(title="Annual Cost ($)"),
        yaxis2=dict(title="Query Volume", overlaying='y', side='right'),
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig_multiyear, use_container_width=True)
    
    # Cost per query trend
    fig_cpq = go.Figure()
    
    fig_cpq.add_trace(go.Scatter(
        x=years_list,
        y=cost_per_query_list,
        mode='lines+markers+text',
        line=dict(color='#dc3545', width=3),
        marker=dict(size=12),
        text=[format_number(v, decimals=4, prefix='$') for v in cost_per_query_list],
        textposition='top center',
        fill='tozeroy',
        fillcolor='rgba(220, 53, 69, 0.1)'
    ))
    
    fig_cpq.update_layout(
        title="Cost per Query Trend",
        height=400,
        yaxis_title="Cost per Query ($)",
        xaxis_title="Year",
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_cpq, use_container_width=True)
    
    # Multi-year summary table
    st.markdown("### 📋 Multi-Year Summary Table")
    
    summary_df = pd.DataFrame({
        'Year': years_list,
        'Query Volume': [format_number(c['queries']) for c in costs],
        'Credits Needed': [format_number(c['credits_needed']) for c in costs],
        'Platform Fee': [format_number(c['platform_fee'], prefix='$') for c in costs],
        'Consumption': [format_number(c['consumption_cost'], prefix='$') for c in costs],
        'Total Cost': [format_number(c['total_cost'], prefix='$') for c in costs],
        'Cost/Query': [format_number(c['cost_per_query'], decimals=4, prefix='$') for c in costs],
        'Monthly Avg': [format_number(c['monthly_cost'], prefix='$') for c in costs]
    })
    
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
    
    # TCO summary
    total_tco = sum([c['total_cost'] for c in costs])
    total_queries = sum([c['queries'] for c in costs])
    avg_cost_per_query = total_tco / total_queries
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            f"{projection_years}-Year TCO",
            format_number(total_tco, prefix='$')
        )
    
    with col2:
        st.metric(
            "Total Queries",
            format_number(total_queries)
        )
    
    with col3:
        st.metric(
            "Avg Cost/Query",
            format_number(avg_cost_per_query, decimals=4, prefix='$')
        )

# Deployment Comparison
st.markdown("## ⚖️ Deployment Model Comparison")

st.markdown("""
    <div class="insight-box">
    <strong>💡 Key Decision:</strong> Deployment model significantly impacts your cost per query due to different query efficiency ratios.
    </div>
""", unsafe_allow_html=True)

# Calculate costs for both deployment models
customer_vpc_costs = calculate_costs(
    annual_queries, platform_fee, credit_cost, 
    DEPLOYMENT_MODELS['Customer VPC']['queries_per_credit'],
    1, 0
)[0]

uniphore_vpc_costs = calculate_costs(
    annual_queries, platform_fee, credit_cost,
    DEPLOYMENT_MODELS['Uniphore VPC']['queries_per_credit'],
    1, 0
)[0]

col1, col2 = st.columns(2)

with col1:
    winner_class = "comparison-winner" if customer_vpc_costs['total_cost'] < uniphore_vpc_costs['total_cost'] else ""
    st.markdown(f"""
        <div class="metric-card {winner_class}">
        <h3>🏢 Customer VPC</h3>
        <p style="font-size: 14px; color: #666;">{DEPLOYMENT_MODELS['Customer VPC']['description']}</p>
        <p style="font-size: 32px; font-weight: bold; color: #007bff; margin: 10px 0;">
        {format_number(customer_vpc_costs['total_cost'], prefix='$')}
        </p>
        <p style="font-size: 14px;">Annual Cost</p>
        <hr>
        <table style="width:100%; text-align: left;">
        <tr><td>Queries/Credit:</td><td style="text-align: right;"><strong>400</strong></td></tr>
        <tr><td>Credits Needed:</td><td style="text-align: right;">{format_number(customer_vpc_costs['credits_needed'])}</td></tr>
        <tr><td>Consumption:</td><td style="text-align: right;">{format_number(customer_vpc_costs['consumption_cost'], prefix='$')}</td></tr>
        <tr><td>Cost/Query:</td><td style="text-align: right;">{format_number(customer_vpc_costs['cost_per_query'], decimals=4, prefix='$')}</td></tr>
        </table>
        <hr>
        <p style="font-size: 12px; color: #28a745;"><strong>✓</strong> {', '.join(DEPLOYMENT_MODELS['Customer VPC']['benefits'])}</p>
        <p style="font-size: 12px; color: #856404;"><strong>⚠</strong> {', '.join(DEPLOYMENT_MODELS['Customer VPC']['considerations'])}</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    winner_class = "comparison-winner" if uniphore_vpc_costs['total_cost'] < customer_vpc_costs['total_cost'] else ""
    st.markdown(f"""
        <div class="metric-card {winner_class}">
        <h3>☁️ Uniphore VPC</h3>
        <p style="font-size: 14px; color: #666;">{DEPLOYMENT_MODELS['Uniphore VPC']['description']}</p>
        <p style="font-size: 32px; font-weight: bold; color: #007bff; margin: 10px 0;">
        {format_number(uniphore_vpc_costs['total_cost'], prefix='$')}
        </p>
        <p style="font-size: 14px;">Annual Cost</p>
        <hr>
        <table style="width:100%; text-align: left;">
        <tr><td>Queries/Credit:</td><td style="text-align: right;"><strong>100</strong></td></tr>
        <tr><td>Credits Needed:</td><td style="text-align: right;">{format_number(uniphore_vpc_costs['credits_needed'])}</td></tr>
        <tr><td>Consumption:</td><td style="text-align: right;">{format_number(uniphore_vpc_costs['consumption_cost'], prefix='$')}</td></tr>
        <tr><td>Cost/Query:</td><td style="text-align: right;">{format_number(uniphore_vpc_costs['cost_per_query'], decimals=4, prefix='$')}</td></tr>
        </table>
        <hr>
        <p style="font-size: 12px; color: #28a745;"><strong>✓</strong> {', '.join(DEPLOYMENT_MODELS['Uniphore VPC']['benefits'])}</p>
        <p style="font-size: 12px; color: #856404;"><strong>⚠</strong> {', '.join(DEPLOYMENT_MODELS['Uniphore VPC']['considerations'])}</p>
        </div>
    """, unsafe_allow_html=True)

# Comparison metrics
cost_difference = abs(customer_vpc_costs['total_cost'] - uniphore_vpc_costs['total_cost'])
cost_difference_pct = (cost_difference / max(customer_vpc_costs['total_cost'], uniphore_vpc_costs['total_cost'])) * 100
cheaper_option = "Customer VPC" if customer_vpc_costs['total_cost'] < uniphore_vpc_costs['total_cost'] else "Uniphore VPC"

st.markdown(f"""
    <div class="insight-box">
    <strong>📊 Comparison Summary:</strong><br>
    • <strong>{cheaper_option}</strong> is {format_number(cost_difference_pct, decimals=1)}% cheaper ({format_number(cost_difference, prefix='$')} savings)<br>
    • Customer VPC offers {DEPLOYMENT_MODELS['Customer VPC']['queries_per_credit'] / DEPLOYMENT_MODELS['Uniphore VPC']['queries_per_credit']:.0f}x better query efficiency<br>
    • Break-even analysis: At {format_number(annual_queries)} queries/year, efficiency drives total cost
    </div>
""", unsafe_allow_html=True)

# Side-by-side comparison chart
comparison_data = {
    'Deployment': ['Customer VPC', 'Uniphore VPC'],
    'Platform Fee': [customer_vpc_costs['platform_fee'], uniphore_vpc_costs['platform_fee']],
    'Consumption': [customer_vpc_costs['consumption_cost'], uniphore_vpc_costs['consumption_cost']],
    'Total': [customer_vpc_costs['total_cost'], uniphore_vpc_costs['total_cost']]
}

fig_comparison = go.Figure()

fig_comparison.add_trace(go.Bar(
    name='Platform Fee',
    x=comparison_data['Deployment'],
    y=comparison_data['Platform Fee'],
    marker_color='#667eea',
    text=[format_number(v, prefix='$') for v in comparison_data['Platform Fee']],
    textposition='inside'
))

fig_comparison.add_trace(go.Bar(
    name='Consumption',
    x=comparison_data['Deployment'],
    y=comparison_data['Consumption'],
    marker_color='#764ba2',
    text=[format_number(v, prefix='$') for v in comparison_data['Consumption']],
    textposition='inside'
))

fig_comparison.update_layout(
    title="Deployment Cost Comparison",
    barmode='stack',
    height=400,
    yaxis_title="Annual Cost ($)",
    showlegend=True
)

st.plotly_chart(fig_comparison, use_container_width=True)

# Export functionality
st.markdown("## 📥 Export Cost Analysis")

col1, col2 = st.columns(2)

with col1:
    # Prepare CSV export
    export_data = []
    for c in costs:
        export_data.append({
            'Year': c['year'],
            'Query Volume': c['queries'],
            'Queries per Credit': queries_per_credit,
            'Credits Needed': c['credits_needed'],
            'Credit Cost': credit_cost,
            'Consumption Cost': c['consumption_cost'],
            'Platform Fee': c['platform_fee'],
            'Total Annual Cost': c['total_cost'],
            'Cost per Query': c['cost_per_query'],
            'Monthly Cost': c['monthly_cost'],
            'Deployment Model': deployment_model
        })
    
    export_df = pd.DataFrame(export_data)
    csv = export_df.to_csv(index=False)
    
    st.download_button(
        label="📊 Download Cost Analysis (CSV)",
        data=csv,
        file_name=f"ai_platform_pricing_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

with col2:
    # Executive summary
    exec_summary = f"""
AI PLATFORM - PRICING SUMMARY
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

CONFIGURATION
Platform Fee: {format_number(platform_fee, prefix='$')}
Credit Cost: ${credit_cost} per credit
Deployment Model: {deployment_model}
Queries per Credit: {queries_per_credit}

YEAR 1 SUMMARY
Annual Query Volume: {format_number(year1['queries'])}
Credits Required: {format_number(year1['credits_needed'])}
Consumption Cost: {format_number(year1['consumption_cost'], prefix='$')}
Total Annual Cost: {format_number(year1['total_cost'], prefix='$')}
Cost per Query: {format_number(year1['cost_per_query'], decimals=4, prefix='$')}
Monthly Cost: {format_number(year1['monthly_cost'], prefix='$')}

{projection_years}-YEAR PROJECTION
Total Cost of Ownership: {format_number(total_tco, prefix='$')}
Total Queries: {format_number(total_queries)}
Average Cost per Query: {format_number(avg_cost_per_query, decimals=4, prefix='$')}
Annual Growth Rate: {growth_rate*100:.0f}%

DEPLOYMENT COMPARISON
Customer VPC: {format_number(customer_vpc_costs['total_cost'], prefix='$')} ({format_number(customer_vpc_costs['cost_per_query'], decimals=4, prefix='$')}/query)
Uniphore VPC: {format_number(uniphore_vpc_costs['total_cost'], prefix='$')} ({format_number(uniphore_vpc_costs['cost_per_query'], decimals=4, prefix='$')}/query)
Difference: {format_number(cost_difference, prefix='$')} ({format_number(cost_difference_pct, decimals=1)}%)
Recommendation: {cheaper_option} for this volume
"""
    
    st.download_button(
        label="📄 Download Executive Summary",
        data=exec_summary,
        file_name=f"pricing_summary_{datetime.now().strftime('%Y%m%d')}.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #6c757d; font-size: 0.9em;'>
    <strong>AI Platform Pricing Calculator</strong> | 
    Consumption-based pricing transparency | 
    Uniphore Business AI Cloud
    </div>
""", unsafe_allow_html=True)
