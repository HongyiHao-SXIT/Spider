import requests
from bs4 import BeautifulSoup
import json
import time
import random
from urllib.parse import quote
import pandas as pd

# 设置请求头，模拟浏览器访问
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

# 代理设置（如果需要）
PROXIES = {
    # 'http': 'http://your_proxy:port',
    # 'https': 'https://your_proxy:port',
}

# 从Google Scholar搜索作者
def search_google_scholar(author_name, max_results=5):
    base_url = "https://scholar.google.com/scholar?"
    query = f"author:{author_name}"
    url = base_url + "q=" + quote(query) + f"&hl=en&as_sdt=0,5&num={max_results}"
    
    try:
        response = requests.get(url, headers=HEADERS, proxies=PROXIES, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Google Scholar results: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    
    for item in soup.select('.gs_ri'):
        title_elem = item.select_one('.gs_rt a')
        if not title_elem:
            continue
            
        title = title_elem.text
        link = title_elem['href']
        authors = item.select_one('.gs_a').text if item.select_one('.gs_a') else ""
        citation_elem = item.select_one('.gs_fl a[href*="cites"]')
        citations = int(citation_elem.text.split()[2]) if citation_elem else 0
        
        result = {
            'title': title,
            'link': link,
            'authors': authors,
            'citations': citations,
            'source': 'Google Scholar'
        }
        results.append(result)
        
        # 避免请求过于频繁
        time.sleep(random.uniform(1, 3))
    
    return results

# 从Semantic Scholar获取作者详细信息
def get_semantic_scholar_author(author_name):
    base_url = "https://api.semanticscholar.org/graph/v1/author/search"
    params = {
        'query': author_name,
        'limit': 5
    }
    
    try:
        response = requests.get(base_url, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Semantic Scholar author data: {e}")
        return []
    
    authors = []
    for author in data.get('data', []):
        author_id = author.get('authorId')
        author_info = {
            'name': author.get('name'),
            'authorId': author_id,
            'affiliations': author.get('affiliations'),
            'homepage': author.get('homepage'),
            'paperCount': author.get('paperCount'),
            'citationCount': author.get('citationCount'),
            'hIndex': author.get('hIndex'),
            'source': 'Semantic Scholar'
        }
        
        # 获取作者的前几篇论文
        if author_id:
            papers = get_semantic_scholar_papers(author_id)
            author_info['papers'] = papers
        
        authors.append(author_info)
        
        # 避免请求过于频繁
        time.sleep(1)
    
    return authors

# 从Semantic Scholar获取作者论文
def get_semantic_scholar_papers(author_id, limit=5):
    base_url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers"
    params = {
        'fields': 'title,url,year,referenceCount,citationCount,publicationTypes,publicationDate',
        'limit': limit
    }
    
    try:
        response = requests.get(base_url, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Semantic Scholar papers: {e}")
        return []
    
    papers = []
    for paper in data.get('data', []):
        paper_info = {
            'title': paper.get('title'),
            'year': paper.get('year'),
            'url': paper.get('url'),
            'referenceCount': paper.get('referenceCount'),
            'citationCount': paper.get('citationCount'),
            'publicationTypes': paper.get('publicationTypes', []),
            'publicationDate': paper.get('publicationDate')
        }
        papers.append(paper_info)
    
    return papers

# 主函数
def main():
    # 示例：搜索特定领域的作者
    domains = ['computer science', 'biology', 'physics', 'economics', 'engineering']
    all_authors_data = []
    
    for domain in domains:
        print(f"Searching for authors in {domain}...")
        
        # 模拟搜索该领域的知名作者
        query = f"top authors in {domain} site:edu"
        search_url = "https://www.google.com/search?q=" + quote(query)
        
        try:
            response = requests.get(search_url, headers=HEADERS, proxies=PROXIES, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error searching for authors in {domain}: {e}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # 这里简化处理，实际应用中需要更复杂的解析
        potential_authors = [a.text for a in soup.select('a') if 'professor' in a.text.lower() or 'dr.' in a.text.lower()]
        
        for author in potential_authors[:3]:  # 每个领域取前3个作者
            print(f"Fetching data for {author}...")
            
            # 从Google Scholar获取数据
            gs_results = search_google_scholar(author)
            
            # 从Semantic Scholar获取数据
            ss_authors = get_semantic_scholar_author(author)
            
            author_data = {
                'name': author,
                'domain': domain,
                'google_scholar': gs_results,
                'semantic_scholar': ss_authors
            }
            
            all_authors_data.append(author_data)
            
            # 保存到JSON文件（增量保存）
            with open('academic_authors.json', 'w', encoding='utf-8') as f:
                json.dump(all_authors_data, f, ensure_ascii=False, indent=2)
            
            # 避免请求过于频繁
            time.sleep(random.uniform(2, 5))
    
    # 保存为CSV文件
    df = pd.json_normalize(all_authors_data, 
                          meta=['name', 'domain'],
                          record_path=['semantic_scholar'],
                          errors='ignore')
    df.to_csv('academic_authors.csv', index=False, encoding='utf-8')
    
    print("Data collection completed. Results saved to academic_authors.json and academic_authors.csv")

if __name__ == "__main__":
    main()