def read_readme():
    try:
        with open('README.md', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "README.md not found"
    except Exception as e:
        return f"Error reading README.md: {str(e)}"

def extract_summary(content):
    summary = []
    
    # Ajout du titre
    summary.append("# RÉSUMÉ DU PROFIL")
    summary.append("\n## À propos de moi")
    summary.append("Développeur passionné par la technologie et l'innovation.")
    
    # Ajout des technologies
    summary.append("\n## Stack Technique")
    summary.append("- Langages: Python, JavaScript")
    summary.append("- Frontend: HTML, CSS")
    summary.append("- Outils: Git, GitHub")
    
    # Ajout des réseaux sociaux
    summary.append("\n## Contact")
    summary.append("GitHub: @rehareha261")
    
    return "\n".join(summary)

def create_main_txt(summary):
    try:
        with open('main.txt', 'w', encoding='utf-8') as file:
            file.write(summary)
        return True
    except Exception as e:
        print(f"Error creating main.txt: {str(e)}")
        return False

# Exécution principale
content = read_readme()
summary = extract_summary(content)
create_main_txt(summary)