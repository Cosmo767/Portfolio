"""
A/B Testing Statistical Visualizations
Interactive plots showing the statistical mechanics behind A/B tests
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)

# Example data
control_visitors = 10000
control_conversions = 500
variant_visitors = 10000
variant_conversions = 580

# Calculate conversion rates
p_control = control_conversions / control_visitors
p_variant = variant_conversions / variant_visitors

# Pooled proportion
p_pooled = (control_conversions + variant_conversions) / (control_visitors + variant_visitors)

# Standard error
se = np.sqrt(p_pooled * (1 - p_pooled) * (1/control_visitors + 1/variant_visitors))

# Z-statistic
z_stat = (p_variant - p_control) / se

# P-value
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print("=" * 60)
print("A/B TEST RESULTS")
print("=" * 60)
print(f"Control Rate:     {p_control:.4f} ({p_control*100:.2f}%)")
print(f"Variant Rate:     {p_variant:.4f} ({p_variant*100:.2f}%)")
print(f"Absolute Diff:    {(p_variant - p_control):.4f}")
print(f"Relative Lift:    {((p_variant - p_control) / p_control * 100):.2f}%")
print(f"Standard Error:   {se:.6f}")
print(f"Z-statistic:      {z_stat:.4f}")
print(f"P-value:          {p_value:.6f}")
print(f"Significant?:     {'YES ✓' if p_value < 0.05 else 'NO ✗'}")
print("=" * 60)

# Create comprehensive visualization
fig = plt.figure(figsize=(16, 12))

# ============================================================================
# PLOT 1: Sampling Distributions
# ============================================================================
ax1 = plt.subplot(3, 2, 1)

# Generate sampling distributions
x = np.linspace(0.03, 0.08, 1000)
control_dist = stats.norm.pdf(x, p_control, np.sqrt(p_control * (1 - p_control) / control_visitors))
variant_dist = stats.norm.pdf(x, p_variant, np.sqrt(p_variant * (1 - p_variant) / variant_visitors))

plt.plot(x, control_dist, 'b-', linewidth=2, label=f'Control (p={p_control:.3f})', alpha=0.7)
plt.plot(x, variant_dist, 'r-', linewidth=2, label=f'Variant (p={p_variant:.3f})', alpha=0.7)
plt.axvline(p_control, color='blue', linestyle='--', alpha=0.5)
plt.axvline(p_variant, color='red', linestyle='--', alpha=0.5)
plt.fill_between(x, control_dist, alpha=0.3, color='blue')
plt.fill_between(x, variant_dist, alpha=0.3, color='red')

plt.xlabel('Conversion Rate', fontsize=11)
plt.ylabel('Probability Density', fontsize=11)
plt.title('Sampling Distributions of Control vs Variant', fontsize=13, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# ============================================================================
# PLOT 2: Z-Test Visualization
# ============================================================================
ax2 = plt.subplot(3, 2, 2)

# Standard normal distribution
x_z = np.linspace(-4, 4, 1000)
y_z = stats.norm.pdf(x_z)

plt.plot(x_z, y_z, 'k-', linewidth=2, label='Standard Normal Distribution')
plt.fill_between(x_z, y_z, alpha=0.2, color='gray')

# Critical regions (alpha = 0.05, two-tailed)
critical_z = 1.96
x_left = x_z[x_z < -critical_z]
x_right = x_z[x_z > critical_z]
plt.fill_between(x_left, stats.norm.pdf(x_left), alpha=0.4, color='red', label='Rejection Region (α=0.05)')
plt.fill_between(x_right, stats.norm.pdf(x_right), alpha=0.4, color='red')

# Our z-statistic
plt.axvline(z_stat, color='green', linewidth=3, linestyle='--', 
            label=f'Our Z-statistic = {z_stat:.2f}')
plt.axvline(-critical_z, color='orange', linewidth=1, linestyle=':', alpha=0.7)
plt.axvline(critical_z, color='orange', linewidth=1, linestyle=':', alpha=0.7)

plt.xlabel('Z-score', fontsize=11)
plt.ylabel('Probability Density', fontsize=11)
plt.title('Z-Test: Where Does Our Statistic Fall?', fontsize=13, fontweight='bold')
plt.legend(fontsize=9)
plt.grid(True, alpha=0.3)

# ============================================================================
# PLOT 3: P-Value Visualization
# ============================================================================
ax3 = plt.subplot(3, 2, 3)

plt.plot(x_z, y_z, 'k-', linewidth=2)
plt.fill_between(x_z, y_z, alpha=0.1, color='gray')

# Shade p-value area (two-tailed)
x_p_left = x_z[x_z < -abs(z_stat)]
x_p_right = x_z[x_z > abs(z_stat)]
plt.fill_between(x_p_left, stats.norm.pdf(x_p_left), alpha=0.6, color='red', 
                 label=f'P-value = {p_value:.4f}')
plt.fill_between(x_p_right, stats.norm.pdf(x_p_right), alpha=0.6, color='red')

plt.axvline(z_stat, color='green', linewidth=2, linestyle='--')
plt.axvline(-z_stat, color='green', linewidth=2, linestyle='--')

# Add text annotation
result_text = "SIGNIFICANT" if p_value < 0.05 else "NOT SIGNIFICANT"
color = "green" if p_value < 0.05 else "red"
plt.text(0, max(y_z) * 0.8, f'{result_text}\n(p < 0.05)' if p_value < 0.05 else f'{result_text}\n(p ≥ 0.05)', 
         ha='center', fontsize=12, fontweight='bold', color=color,
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.xlabel('Z-score', fontsize=11)
plt.ylabel('Probability Density', fontsize=11)
plt.title('P-Value: Probability of Observing This Result by Chance', fontsize=13, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

# ============================================================================
# PLOT 4: Confidence Intervals
# ============================================================================
ax4 = plt.subplot(3, 2, 4)

# Calculate 95% confidence intervals
ci_control = 1.96 * np.sqrt(p_control * (1 - p_control) / control_visitors)
ci_variant = 1.96 * np.sqrt(p_variant * (1 - p_variant) / variant_visitors)

categories = ['Control', 'Variant']
rates = [p_control, p_variant]
errors = [ci_control, ci_variant]
colors = ['#3498db', '#e74c3c']

bars = plt.bar(categories, [r * 100 for r in rates], color=colors, alpha=0.7, 
               edgecolor='black', linewidth=2)
plt.errorbar(categories, [r * 100 for r in rates], yerr=[e * 100 for e in errors], 
             fmt='none', ecolor='black', capsize=10, linewidth=2)

# Add value labels
for i, (bar, rate, err) in enumerate(zip(bars, rates, errors)):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{rate*100:.2f}%\n±{err*100:.2f}%',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.ylabel('Conversion Rate (%)', fontsize=11)
plt.title('Conversion Rates with 95% Confidence Intervals', fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.ylim(0, max(rates) * 120)

# ============================================================================
# PLOT 5: Effect Size and Statistical Power
# ============================================================================
ax5 = plt.subplot(3, 2, 5)

# Create distributions for null and alternative hypotheses
diff_null = 0
diff_observed = p_variant - p_control
se_diff = se

x_diff = np.linspace(-3*se_diff, diff_observed + 3*se_diff, 1000)
null_dist = stats.norm.pdf(x_diff, diff_null, se_diff)
alt_dist = stats.norm.pdf(x_diff, diff_observed, se_diff)

plt.plot(x_diff * 100, null_dist / (se_diff * 100), 'b-', linewidth=2, 
         label='Null Hypothesis (No Difference)', alpha=0.7)
plt.plot(x_diff * 100, alt_dist / (se_diff * 100), 'r-', linewidth=2, 
         label='Alternative Hypothesis (True Difference)', alpha=0.7)

plt.fill_between(x_diff * 100, null_dist / (se_diff * 100), alpha=0.2, color='blue')
plt.fill_between(x_diff * 100, alt_dist / (se_diff * 100), alpha=0.2, color='red')

# Critical value for rejection
critical_value = 1.96 * se_diff
plt.axvline(critical_value * 100, color='green', linestyle='--', linewidth=2,
            label=f'Critical Value (α=0.05)')

# Shade Type I error (false positive)
x_type1 = x_diff[x_diff > critical_value]
plt.fill_between(x_type1 * 100, stats.norm.pdf(x_type1, diff_null, se_diff) / (se_diff * 100), 
                 alpha=0.4, color='orange', label='Type I Error (α)')

# Shade Type II error (false negative)
x_type2 = x_diff[x_diff < critical_value]
plt.fill_between(x_type2 * 100, stats.norm.pdf(x_type2, diff_observed, se_diff) / (se_diff * 100), 
                 alpha=0.4, color='purple', label='Type II Error (β)')

plt.xlabel('Difference in Conversion Rate (%)', fontsize=11)
plt.ylabel('Probability Density', fontsize=11)
plt.title('Statistical Power: Type I vs Type II Errors', fontsize=13, fontweight='bold')
plt.legend(fontsize=9)
plt.grid(True, alpha=0.3)

# ============================================================================
# PLOT 6: Sample Size vs Power Curve
# ============================================================================
ax6 = plt.subplot(3, 2, 6)

# Calculate power for different sample sizes
sample_sizes = np.linspace(1000, 50000, 100)
powers = []

for n in sample_sizes:
    # Standard error for this sample size
    se_n = np.sqrt(p_pooled * (1 - p_pooled) * (2 / n))
    # Non-centrality parameter
    ncp = diff_observed / se_n
    # Power = 1 - β (probability of correctly rejecting null)
    power = 1 - stats.norm.cdf(1.96 - ncp)
    powers.append(power)

plt.plot(sample_sizes, powers, 'b-', linewidth=3, label='Statistical Power')
plt.axhline(0.8, color='green', linestyle='--', linewidth=2, label='Target Power (80%)')
plt.axhline(0.95, color='orange', linestyle='--', linewidth=1, label='High Power (95%)')
plt.axvline(control_visitors, color='red', linestyle=':', linewidth=2, 
            label=f'Current Sample Size ({control_visitors:,})')

# Find sample size for 80% power
power_80_idx = np.argmin(np.abs(np.array(powers) - 0.8))
sample_for_80 = sample_sizes[power_80_idx]
plt.plot(sample_for_80, 0.8, 'go', markersize=12)
plt.annotate(f'n={sample_for_80:,.0f} for 80% power', 
             xy=(sample_for_80, 0.8), xytext=(sample_for_80 + 5000, 0.65),
             arrowprops=dict(arrowstyle='->', color='green', lw=2),
             fontsize=10, fontweight='bold')

plt.xlabel('Sample Size per Variant', fontsize=11)
plt.ylabel('Statistical Power (1 - β)', fontsize=11)
plt.title('How Sample Size Affects Statistical Power', fontsize=13, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(0, 1)

# ============================================================================
# Final adjustments
# ============================================================================
plt.tight_layout()
plt.savefig('ab_test_statistical_breakdown.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved as 'ab_test_statistical_breakdown.png'")
plt.show()

# ============================================================================
# BONUS: Create a simplified explanation plot
# ============================================================================
fig2, axes = plt.subplots(2, 2, figsize=(14, 10))

# Simplified Z-test explanation
ax = axes[0, 0]
x_simple = np.linspace(-4, 4, 1000)
y_simple = stats.norm.pdf(x_simple)
ax.plot(x_simple, y_simple, 'k-', linewidth=2)
ax.fill_between(x_simple, y_simple, alpha=0.2, color='gray')
ax.axvline(z_stat, color='red', linewidth=3, label=f'Our Z-statistic = {z_stat:.2f}')
ax.axvline(-1.96, color='green', linestyle='--', label='Critical values (±1.96)')
ax.axvline(1.96, color='green', linestyle='--')
ax.set_title('What is a Z-Test?', fontsize=14, fontweight='bold')
ax.set_xlabel('Standard Deviations from Mean')
ax.set_ylabel('Probability')
ax.legend()
ax.grid(True, alpha=0.3)
ax.text(0, max(y_simple) * 0.5, 
        'Z-test asks:\n"How many standard deviations\nis our result from zero?"',
        ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat'))

# What is p-value?
ax = axes[0, 1]
ax.plot(x_simple, y_simple, 'k-', linewidth=2)
x_shade = x_simple[np.abs(x_simple) > abs(z_stat)]
ax.fill_between(x_shade, stats.norm.pdf(x_shade), alpha=0.5, color='red', 
                label=f'P-value area = {p_value:.4f}')
ax.set_title('What is a P-Value?', fontsize=14, fontweight='bold')
ax.set_xlabel('Z-score')
ax.set_ylabel('Probability')
ax.legend()
ax.grid(True, alpha=0.3)
ax.text(0, max(y_simple) * 0.5,
        'P-value =\nProbability of seeing this result\n(or more extreme)\nif there\'s truly NO difference',
        ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue'))

# Formula breakdown
ax = axes[1, 0]
ax.axis('off')
formula_text = f"""
Z-TEST FORMULA BREAKDOWN

1. Calculate Conversion Rates:
   Control:  {control_conversions}/{control_visitors} = {p_control:.4f}
   Variant:  {variant_conversions}/{variant_visitors} = {p_variant:.4f}

2. Pool the Proportions:
   p_pooled = ({control_conversions} + {variant_conversions}) / ({control_visitors} + {variant_visitors})
            = {p_pooled:.4f}

3. Calculate Standard Error:
   SE = √[p_pooled × (1 - p_pooled) × (1/n₁ + 1/n₂)]
      = {se:.6f}

4. Calculate Z-statistic:
   Z = (p_variant - p_control) / SE
     = ({p_variant:.4f} - {p_control:.4f}) / {se:.6f}
     = {z_stat:.4f}

5. Find P-value:
   P-value = 2 × P(Z > |{z_stat:.2f}|) = {p_value:.6f}
   
6. Decision:
   {'✓ REJECT null hypothesis (significant)' if p_value < 0.05 else '✗ FAIL TO REJECT null (not significant)'}
   Variant {'IS' if p_value < 0.05 else 'IS NOT'} statistically better than Control
"""
ax.text(0.05, 0.95, formula_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Decision guide
ax = axes[1, 1]
ax.axis('off')
decision_text = f"""
INTERPRETATION GUIDE

Statistical Significance:
• P-value: {p_value:.6f}
• Threshold: 0.05 (95% confidence)
• Result: {'SIGNIFICANT ✓' if p_value < 0.05 else 'NOT SIGNIFICANT ✗'}

What This Means:
{'There is less than 5% probability this difference' if p_value < 0.05 else 'There is more than 5% probability this difference'}
{'is due to random chance. We can confidently' if p_value < 0.05 else 'is due to random chance. We cannot confidently'}
{'say the Variant is better.' if p_value < 0.05 else 'say the Variant is better.'}

Practical Significance:
• Absolute lift: {(p_variant - p_control)*100:.2f} percentage points
• Relative lift: {((p_variant - p_control) / p_control * 100):.1f}%

Recommendation:
{f'✓ Roll out Variant B to all users' if p_value < 0.05 else '✗ Keep current version (Control A)'}
{f'  Expected impact: {((p_variant - p_control) * variant_visitors):.0f} extra conversions' if p_value < 0.05 else '  Consider testing a more dramatic change'}
{f'  per {variant_visitors:,} visitors' if p_value < 0.05 else ''}
"""
ax.text(0.05, 0.95, decision_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='lightgreen' if p_value < 0.05 else 'lightcoral', alpha=0.7))

plt.tight_layout()
plt.savefig('ab_test_explained.png', dpi=300, bbox_inches='tight')
print("✓ Explanation saved as 'ab_test_explained.png'")
plt.show()

print("\n" + "="*60)
print("VISUALIZATIONS COMPLETE!")
print("="*60)
print("Created 2 comprehensive visualizations:")
print("  1. ab_test_statistical_breakdown.png - 6 detailed plots")
print("  2. ab_test_explained.png - Simple explanations")
print("="*60)
