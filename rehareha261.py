def read_readme():
    try:
        with open('README.md', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "README.md not found"
    except Exception as e:
        return f"Error reading README.md: {str(e)}"

def extract_main_sections(content):
    sections = {
        'About Me': '',
        'Socials': '',
        'Tech Stack': ''
    }
    
    lines = content.split('\n')
    current_section = None
    
    for line in lines:
        if line.startswith('###') or line.startswith('##'):
            section_name = line.strip('#').strip()
            if section_name in sections:
                current_section = section_name
        elif current_section and line.strip():
            sections[current_section] += line.strip() + '\n'
    
    return sections

def create_summary():
    content = read_readme()
    sections = extract_main_sections(content)
    
    summary = "# Résumé du README\n\n"
    for section, text in sections.items():
        if text:
            summary += f"## {section}\n{text}\n"
    
    return summary

if __name__ == "__main__":
    summary = create_summary()
    with open('main.txt', 'w', encoding='utf-8') as file:
        file.write(summary)