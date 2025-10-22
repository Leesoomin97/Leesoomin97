# 👋 Hi, I'm **Soomin Lee (이수민)**
**Data Scientist / MLOps Learner**

> 데이터를 이해하고, 시스템을 설계하며, 서비스를 완성하는 과정을 즐깁니다.  
> *I build things to understand how they work — then make them work better.*

---

## 📫 Contact & Links
- ✉️ **Email:** milpasoomin@gmail.com 
- 🌐 **Blog:** [네이버 블로그]https://blog.naver.com/milpa/ 
- 📄 **Resume:** [이력서 보기](./resume/soomin_lee_resume.pdf)  
- 🧠 **Learning Archive:** [Paper Notes](./paper-notes) · [Study Logs](./study-logs)

---

## 🧩 Projects

### 🏙️ [Seoul Apartment Price Prediction](https://github.com/Leesoomin97/upstage-ml-regression-ml_3-soomin)
**Type:** Practice Project (Bootcamp Internal)  
**Goal:** 서울시 실거래가 데이터를 활용한 아파트 가격 예측  
**Stack:** Python, Pandas, LightGBM, XGBoost, CatBoost  

#### Highlights
- 피처 엔지니어링 및 다양한 회귀 모델 비교  
- Linear, RF, LGBM, XGBoost, CatBoost 모델 성능 분석  
- 앙상블 기반 일반화 성능 향상 및 Feature 영향도 해석  

---

### 🎮 [Game Recommendation MLOps Project](https://github.com/Leesoomin97/mlops-game_recommendation_project_team3)
**Type:** MLOps Project (Team + Personal)  
**Goal:** RAWG API 기반 게임 추천 시스템 구축 및 배포 자동화  
**Stack:** Airflow, Docker, S3, EC2, FastAPI, MySQL, GitHub Actions, Slack Webhook  

#### 🧱 Team Version
- 완전한 컨테이너 기반 **3단 구조** (개발 → 오케스트레이션 → 배포)  
- GitHub Actions → DockerHub → EC2로 이어지는 **CI/CD 파이프라인**  
- Airflow DAG 자동화: 데이터 준비 → 모델 학습 → 추천 저장 → Slack 알림  
- EC2 분리 아키텍처 (오케스트레이션 서버 / 서비스 서버)  
- S3 + MySQL 중심의 **데이터·모델 버전 관리**

#### ↳ 🧪 [Personal Prototype](https://github.com/Leesoomin97/Previous_version_mlops_game_recommendation_soomin)
- 팀 버전의 개인 실험 및 확장 버전  
- Airflow DAG 설계, GitHub Actions CI 구축 성공  
- 로컬 환경에서 모델링 및 추천 로직 검증  

---

### 💰 [Toss CTR Prediction](https://github.com/Leesoomin97/toss_ctr_dacon_project)
**Type:** Competition Project (DACON, Completed)  
**Goal:** 광고 클릭 확률 예측 모델 개발  
**Stack:** LightGBM, XGBoost, Deep & Cross Network (DCN), PyTorch  

#### Highlights
- 대규모 로그 데이터 기반 CTR Feature Engineering  
- Sequence, Cross Feature, Diversity Ratio 등 고급 피처 설계  
- K-Fold Ensemble 및 Meta Blending으로 최종 모델 완성  
- 🏆 **Leaderboard:** 2571명 중 313등 → 상위 약 **12%**

---

## 📂 Repository Structure
```plaintext
leesoomin97/
├── projects/                                   # 프로젝트 모음
│   ├── upstage-ml-regression-ml_3-soomin/      ← [Seoul Apartment Price Prediction](https://github.com/Leesoomin97/upstage-ml-regression-ml_3-soomin)
│   ├── mlops-game_recommendation_project_team3/← [Game Recommendation MLOps - Team Project](https://github.com/Leesoomin97/mlops-game_recommendation_project_team3)
│   │   └── Previous_version_mlops_game_recommendation_soomin/ ← [Personal Prototype](https://github.com/Leesoomin97/Previous_version_mlops_game_recommendation_soomin)
│   └── toss-ctr-competition/                   ← [Toss CTR Prediction](https://github.com/Leesoomin97/toss-ctr-competition)
├── study-logs/                                 # 학습 회고 및 기술 노트
├── paper-notes/                                # 논문 요약 및 리서치 정리
├── resume/                                     # 이력서 및 포트폴리오
└── README.md                                   # 메인 프로필 (현재 이 파일)
```

---

> 📌 *“단순히 모델을 만드는 것”이 아니라 “시스템 전체를 이해하며 개선하는 사람”이 되고자 합니다.*
