# update_main_readme.py
import os
from datetime import datetime

# 각 폴더 설명
FOLDER_INFO = {
    "projects": "실험, 구현한 프로젝트 및 대회 활동",
    "study-logs": "학습 회고 및 기술 노트",
    "paper-notes": "논문 요약 및 리서치 정리",
    "resume": "이력서 및 포트폴리오",
}

# 기본 헤더
HEADER = """# 🏗️ Leesoomin97 GitHub Portfolio

👋 Hi, I'm **Soomin Lee (이수민)**  
Data Scientist / MLOps Learner

> 데이터의 흐름을 이해하고, 시스템을 설계하며, 서비스를 완성하는 과정을 즐깁니다.  
> I build things to understand how they work — then make them work better.

📅 마지막 업데이트: {date}

---
"""

def get_folders(base="."):
    """루트 하위 폴더 목록 가져오기"""
    folders = [f for f in os.listdir(base) if os.path.isdir(f)]
    # 보기 좋게 정렬 (projects, study-logs, paper-notes, resume 순)
    order = ["projects", "study-logs", "paper-notes", "resume"]
    return sorted(folders, key=lambda x: order.index(x) if x in order else 99)

def generate_readme():
    today = datetime.now().strftime("%Y-%m-%d")
    content = HEADER.format(date=today)

    content += "## 📂 Repository Structure\n\n"
    content += "```bash\nleesoomin97/\n"
    for folder in get_folders():
        desc = FOLDER_INFO.get(folder, "")
        content += f"├── {folder}/"
        if desc:
            content += f"    # {desc}"
        content += "\n"
    content += "└── README.md   # 메인 프로필 (이 파일)\n```\n\n"

    content += "## 🔗 Quick Access\n\n"
    for folder, desc in FOLDER_INFO.items():
        if os.path.exists(folder):
            content += f"- [{folder}/]({folder}/) — {desc}\n"
    content += "\n"

    content += "---\n> _자동 생성된 README (update_main_readme.py 실행 결과)_\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ 루트 README.md 자동 갱신 완료!")

if __name__ == "__main__":
    generate_readme()
