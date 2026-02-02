#!/usr/bin/env python3
"""
Issue-Based Commentary Content Generator
Creates solution-focused articles on social issues with ethical monetization
"""

import os
import random
import re
from datetime import datetime
from urllib.parse import quote

# Content categories
CATEGORIES = {
    "cost-of-living": {
        "name": "Cost of Living & Corporate Tricks",
        "description": "Analyzing fees, shrinkflation, and corporate practices affecting everyday budgets"
    },
    "workers-workplace": {
        "name": "Workers & Workplace Power",
        "description": "Rights, negotiation, and organizing basics for workers"
    },
    "healthcare-community": {
        "name": "Healthcare & Community",
        "description": "Access, prevention, mutual aid, and navigating healthcare systems"
    },
    "climate-solutions": {
        "name": "Climate Solutions That Work",
        "description": "Local wins and simple policy explanations"
    },
    "privacy-rights": {
        "name": "Privacy & Digital Rights",
        "description": "Beginner-friendly cybersecurity and privacy tips"
    },
    "civic-basics": {
        "name": "Civic Basics",
        "description": "How local government works and constructive participation"
    }
}

# Affiliate product categories
AFFILIATE_PRODUCTS = {
    "budgeting-tools": [
        {"name": "Budgeting Notebook", "description": "Personal finance tracking", "url": "#"},
        {"name": "Expense Tracking App Subscription", "description": "Digital budgeting tools", "url": "#"}
    ],
    "privacy-tools": [
        {"name": "VPN Service", "description": "Internet privacy protection", "url": "#"},
        {"name": "Password Manager", "description": "Secure password storage", "url": "#"}
    ],
    "energy-efficiency": [
        {"name": "Smart Thermostat", "description": "Energy-saving home temperature control", "url": "#"},
        {"name": "LED Bulbs Pack", "description": "Energy-efficient lighting", "url": "#"}
    ],
    "household-items": [
        {"name": "Reusable Water Bottle", "description": "Reduce plastic waste", "url": "#"},
        {"name": "Beeswax Wraps", "description": "Sustainable food storage", "url": "#"}
    ],
    "worker-gear": [
        {"name": "Ergonomic Keyboard", "description": "Workplace injury prevention", "url": "#"},
        {"name": "Anti-fatigue Mat", "description": "Comfort for standing work", "url": "#"}
    ],
    "learning-resources": [
        {"name": "Understanding Healthcare Guide", "description": "Navigate medical systems", "url": "#"},
        {"name": "Civic Participation Handbook", "description": "Engage with local government", "url": "#"}
    ]
}

# Article templates
ARTICLE_TEMPLATES = [
    {
        "title": "The Hidden Costs of {service}: How Fee Creep Is Draining Your Wallet",
        "category": "cost-of-living",
        "hook": "You've probably noticed that basic services seem to be costing more without providing better value. From bank fees to subscription services, companies are using subtle tactics to increase revenue without significantly improving their offerings.",
        "what_wrong": "Many companies now rely on fee creep - the gradual addition of small charges that compound over time. What started as a simple monthly service now includes maintenance fees, processing fees, and convenience charges that weren't clearly disclosed upfront.",
        "why_happens": "This practice has become normalized because individual fees appear small, making consumers less likely to scrutinize them. Additionally, regulatory oversight has not kept pace with evolving business models, allowing companies to exploit loopholes.",
        "what_working": "Some states have implemented fee transparency laws requiring companies to bundle all costs upfront. Cities like San Francisco have passed ordinances requiring banks to disclose total annual costs for checking accounts.",
        "actions": [
            "Audit your monthly subscriptions and fees annually",
            "Switch to credit unions or community banks with lower fees",
            "Use fee-free ATMs and avoid out-of-network charges",
            "Negotiate recurring service contracts",
            "Support businesses with transparent pricing",
            "Advocate for stronger fee disclosure regulations"
        ],
        "sources": [
            {"title": "Fee Creep in Financial Services", "url": "https://example.com", "date": "2024-01-15"},
            {"title": "Consumer Protection Report", "url": "https://example.com", "date": "2024-02-01"}
        ]
    },
    {
        "title": "Know Your Rights: Essential Worker Protections You Should Understand",
        "category": "workers-workplace",
        "hook": "Despite common misconceptions, many workers are unaware of the protections and benefits they're legally entitled to. Understanding your workplace rights can lead to better conditions and compensation without confrontation.",
        "what_wrong": "Millions of workers operate without fully understanding their legal protections, leaving them vulnerable to wage theft, unsafe conditions, and discriminatory practices. This knowledge gap disproportionately affects low-wage workers and those in non-traditional employment arrangements.",
        "why_happens": "Employers often don't proactively educate workers about rights, and many employees fear retaliation if they ask questions. Complex labor laws and inconsistent enforcement also contribute to this information asymmetry.",
        "what_working": "Several states have implemented worker rights education programs. California's Labor Commissioner office has launched multilingual resources that have helped thousands of workers recover lost wages.",
        "actions": [
            "Research your state's labor laws and minimum wage requirements",
            "Document your work hours and pay stubs carefully",
            "Connect with local worker centers for free resources",
            "Join or form workplace committees for collective advocacy",
            "Report violations to appropriate agencies anonymously if needed",
            "Support ballot initiatives that strengthen worker protections"
        ],
        "sources": [
            {"title": "State Worker Rights Comparison", "url": "https://example.com", "date": "2024-01-20"},
            {"title": "Labor Department Compliance Report", "url": "https://example.com", "date": "2024-02-05"}
        ]
    },
    {
        "title": "Navigating Healthcare: A Guide to Getting Quality Care Without Bankruptcy",
        "category": "healthcare-community",
        "hook": "The American healthcare system is notoriously difficult to navigate, often leaving patients confused about options and costs. However, there are practical strategies that can help you access quality care while managing expenses.",
        "what_wrong": "Many Americans delay necessary medical care due to cost concerns, leading to worse health outcomes and higher long-term costs. The complexity of insurance networks, prior authorization requirements, and surprise billing make healthcare access unpredictable and financially risky.",
        "why_happens": "The fragmented nature of American healthcare, with multiple payers and providers operating independently, creates inefficiencies and administrative burdens that drive up costs for everyone involved.",
        "what_working": "Some communities have developed successful healthcare navigation programs. Oregon's Patient Navigator program has reduced emergency room visits by 30% among participants by helping them access appropriate primary care.",
        "actions": [
            "Choose in-network providers to avoid surprise bills",
            "Request itemized bills and dispute errors",
            "Apply for financial assistance programs if eligible",
            "Consider high-deductible plans with HSA for predictable care",
            "Use telemedicine for minor issues to save costs",
            "Shop around for non-emergency procedures"
        ],
        "sources": [
            {"title": "Healthcare Navigation Best Practices", "url": "https://example.com", "date": "2024-01-25"},
            {"title": "Medical Debt Impact Study", "url": "https://example.com", "date": "2024-02-10"}
        ]
    }
]

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def generate_article(topic=None):
    """Generate a complete article based on templates"""
    if topic:
        # Use provided topic if available
        template = topic
    else:
        # Select random template
        template = random.choice(ARTICLE_TEMPLATES)
    
    # Fill in template variables if needed
    if '{service}' in template['title']:
        services = ['Banking', 'Streaming', 'Cell Phone', 'Gym Memberships', 'Insurance']
        service = random.choice(services)
        title = template['title'].format(service=service)
    else:
        title = template['title']
    
    category_key = template['category']
    category_info = CATEGORIES[category_key]
    
    # Generate slug
    slug = slugify(title)
    
    # Generate meta description
    meta_description = f"{template['hook'][:100]}... Practical solutions for {category_info['description'].lower()}"
    
    # Select random affiliate products for this post
    affiliate_category = random.choice(list(AFFILIATE_PRODUCTS.keys()))
    selected_affiliates = random.sample(AFFILIATE_PRODUCTS[affiliate_category], min(2, len(AFFILIATE_PRODUCTS[affiliate_category])))
    
    article = {
        "title": title,
        "slug": slug,
        "meta_description": meta_description,
        "date": datetime.now().strftime("%B %d, %Y"),
        "category": category_key,
        "category_name": category_info["name"],
        "hook": template["hook"],
        "what_wrong": template["what_wrong"],
        "why_happens": template["why_happens"],
        "what_working": template["what_working"],
        "actions": template["actions"],
        "sources": template["sources"],
        "affiliate_products": selected_affiliates,
        "related_posts": []  # Will be populated later
    }
    
    return article

def save_article_to_file(article, base_dir="posts"):
    """Save the generated article as an HTML file"""
    os.makedirs(os.path.join(base_dir, article['category']), exist_ok=True)
    
    # Read the post template
    with open('templates/post.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Format the content
    content_html = f"""
    <article class="content-section">
        <h1>{article['title']}</h1>
        <div class="date">{article['date']}</div>
        <span class="category-tag">{article['category_name']}</span>
        
        <div class="hook">
            {article['hook']}
        </div>
        
        <h2 class="section-title">What's Wrong</h2>
        <div class="what-wrong">
            <p>{article['what_wrong']}</p>
        </div>
        
        <h2 class="section-title">Why It Happens</h2>
        <div class="why-happens">
            <p>{article['why_happens']}</p>
        </div>
        
        <h2 class="section-title">What's Working Somewhere</h2>
        <div class="what-working">
            <p>{article['what_working']}</p>
        </div>
        
        <h2 class="section-title">What You Can Do This Week</h2>
        <div class="what-you-can-do">
            <ul class="actions-list">
                {''.join([f'<li>{action}</li>' for action in article['actions']])}
            </ul>
        </div>
        
        <div class="affiliate-disclaimer">
            <strong>Affiliate Notice:</strong> This post contains links to products that can help with the issues discussed. Purchases through these links may earn a small commission that supports our continued work.
            <div style="margin-top: 1rem;">
                <h3>Products That Can Help:</h3>
                {''.join([f'<p><a href="{prod["url"]}" target="_blank">{prod["name"]}</a>: {prod["description"]}</p>' for prod in article['affiliate_products']])}
            </div>
        </div>
        
        <h2 class="section-title">Sources</h2>
        <div class="sources">
            <ul>
                {''.join([f'<li><a href="{source["url"]}">{source["title"]}</a> ({source["date"]})</li>' for source in article['sources']])}
            </ul>
        </div>
        
        <div class="related-posts">
            <h3>Related Articles</h3>
            <p>Explore more articles in the <a href="/category/{article['category']}/">{article['category_name']}</a> category.</p>
        </div>
    </article>
    """
    
    # Replace template variables
    html_content = template.replace('{{TITLE}}', article['title'])
    html_content = html_content.replace('{{META_DESCRIPTION}}', article['meta_description'])
    html_content = html_content.replace('{{CONTENT}}', content_html)
    
    # Save the article
    filename = os.path.join(base_dir, article['category'], f"{article['slug']}.html")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filename

def update_index_page(new_post=None):
    """Update the index page with the latest posts"""
    # Read index template
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Get list of recent posts
    post_links = []
    
    for category in CATEGORIES:
        category_dir = os.path.join('posts', category)
        if os.path.exists(category_dir):
            posts = sorted(os.listdir(category_dir), reverse=True)[:5]  # Get 5 most recent from each category
            for post in posts[:2]:  # Take 2 from each category
                if post.endswith('.html'):
                    slug = post[:-5]  # Remove .html
                    # Need to extract title from the file
                    post_path = os.path.join(category_dir, post)
                    with open(post_path, 'r', encoding='utf-8') as pf:
                        content = pf.read()
                        # Extract title from the content
                        import re
                        title_match = re.search(r'<h1>(.*?)</h1>', content)
                        title = title_match.group(1) if title_match else slug.replace('-', ' ').title()
                    
                    post_links.append({
                        'title': title,
                        'url': f"/{category}/{slug}/",
                        'date': '2024-02-01',  # Placeholder - would need to extract from file
                        'category': CATEGORIES[category]['name']
                    })
    
    # Limit to 6 most recent posts
    post_links = post_links[:6]
    
    # Create HTML for post grid
    posts_html = ""
    for post in post_links:
        posts_html += f"""
        <div class="post-card">
            <span class="category-tag">{post['category']}</span>
            <h3><a href="{post['url']}">{post['title']}</a></h3>
            <div class="date">{post['date']}</div>
            <p>Practical solutions and insights on this important issue...</p>
        </div>
        """
    
    # Replace in template
    html_content = template.replace('{{POSTS}}', posts_html)
    
    # Save index page
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_sitemap():
    """Generate sitemap.xml for SEO"""
    urls = [
        {"loc": "https://example.com/", "lastmod": datetime.now().strftime("%Y-%m-%d"), "changefreq": "daily", "priority": "1.0"},
        {"loc": "https://example.com/affiliate-disclosure/", "lastmod": datetime.now().strftime("%Y-%m-%d"), "changefreq": "monthly", "priority": "0.8"},
    ]
    
    # Add category pages
    for cat_key, cat_info in CATEGORIES.items():
        urls.append({
            "loc": f"https://example.com/category/{cat_key}/",
            "lastmod": datetime.now().strftime("%Y-%m-%d"),
            "changefreq": "weekly",
            "priority": "0.9"
        })
    
    # Add posts
    for category in CATEGORIES:
        category_dir = os.path.join('posts', category)
        if os.path.exists(category_dir):
            posts = os.listdir(category_dir)
            for post in posts:
                if post.endswith('.html'):
                    slug = post[:-5]
                    urls.append({
                        "loc": f"https://example.com/{category}/{slug}/",
                        "lastmod": datetime.now().strftime("%Y-%m-%d"),
                        "changefreq": "monthly",
                        "priority": "0.7"
                    })
    
    # Create sitemap XML
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url in urls:
        sitemap_xml += f'  <url>\n'
        sitemap_xml += f'    <loc>{url["loc"]}</loc>\n'
        sitemap_xml += f'    <lastmod>{url["lastmod"]}</lastmod>\n'
        sitemap_xml += f'    <changefreq>{url["changefreq"]}</changefreq>\n'
        sitemap_xml += f'    <priority>{url["priority"]}</priority>\n'
        sitemap_xml += f'  </url>\n'
    
    sitemap_xml += '</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)

def generate_rss_feed():
    """Generate RSS feed for the site"""
    # This would typically pull from actual posts, but for now we'll create a template
    rss_content = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>Better World Commentary</title>
  <link>https://example.com</link>
  <description>Positive, solution-focused commentary on today's issues</description>
  <language>en-us</language>
  <pubDate>{pub_date}</pubDate>
  <lastBuildDate>{build_date}</lastBuildDate>
  <generator>Custom RSS Generator</generator>
</channel>
</rss>'''.format(
        pub_date=datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z"),
        build_date=datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
    )
    
    with open('feed.rss', 'w', encoding='utf-8') as f:
        f.write(rss_content)

def main():
    """Generate a new article and update the site"""
    print("Generating new issue-based commentary article...")
    
    # Generate a new article
    article = generate_article()
    filename = save_article_to_file(article)
    
    print(f"Generated article: {filename}")
    
    # Update the index page
    update_index_page(article)
    print("Updated index page with new article")
    
    # Generate sitemap
    generate_sitemap()
    print("Generated sitemap.xml")
    
    # Generate RSS feed
    generate_rss_feed()
    print("Generated RSS feed")
    
    print("\nSite generation complete!")
    print("Files created:")
    print(f"- Article: {filename}")
    print("- Index page: index.html")
    print("- Sitemap: sitemap.xml")
    print("- RSS feed: feed.rss")

if __name__ == "__main__":
    main()