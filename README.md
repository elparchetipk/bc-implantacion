# Software Deployment Bootcamp

![Banner](./assets/banner-bootcamp.svg)

## 📋 Overview

Intensive 9-week bootcamp focused on **Software Deployment competency**, designed to train participants in planning and executing software deployment activities according to system conditions.

### Learning Outcome

**Plan software deployment activities according to system conditions**

---

## 🎯 Key Skills

- Prepare technology platforms based on selected operating systems
- Verify minimum hardware requirements for developed software
- Design data migration plans according to implementation conditions
- Design data backup plans to mitigate risks
- Develop installation plans based on software characteristics

---

## 🗓️ Program Structure

| Week    | Topic                        | Focus Area                                                  |
| ------- | ---------------------------- | ----------------------------------------------------------- |
| **1-2** | Hardware & Platforms         | Server hardware, minimum requirements, platform preparation |
| **3-4** | Server Operating Systems     | Linux Server, Windows Server, OS selection                  |
| **5**   | Containers & Server Software | Docker, Docker Compose, PostgreSQL 15+, Nginx               |
| **6**   | Hosting & Domains            | Hosting types, domain management, FTP, CMS                  |
| **7**   | Data Migration & Backup      | Migration plans, backup strategies, restoration             |
| **8**   | Installation Planning        | Installation plan development, requirements verification    |
| **9**   | Integration & Final Project  | Complete system deployment, evaluation                      |

---

## 🛠️ Technology Stack

- **Containers**: Docker & Docker Compose v2
- **Database**: PostgreSQL 15+
- **Web Server**: Nginx
- **API**: REST Architecture
- **Operating Systems**: Ubuntu Server, Rocky Linux
- **Version Control**: Git with Conventional Commits

---

## 🚀 Quick Start

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd bc-implantacion
   ```

2. **Review documentation**

   - [Quick Start Guide](./_docs/QUICK-START.md)
   - [Copilot Instructions](./.github/copilot-instructions.md)

3. **Set up auto-commit (optional)**
   ```bash
   ./scripts/install-cron.sh
   ```

---

## 📚 Documentation

- **[Quick Start Guide](./_docs/QUICK-START.md)** - Installation and setup
- **[SVG Naming Convention](./_docs/CAMBIOS-NOMENCLATURA-SVG.md)** - Graphic resources guidelines
- **[Code Example](./_docs/ejemplo-codigo-comentado.yml)** - Educational code template
- **[Scripts Documentation](./scripts/README.md)** - Automation scripts
- **[Copilot Instructions](./.github/copilot-instructions.md)** - AI-assisted development guidelines

---

## 📂 Repository Structure

```
bc-implantacion/
├── bootcamp/              # Bootcamp content (9 weeks)
│   └── semana-XX/         # Weekly content
│       ├── 1-teoria/      # Theoretical material
│       ├── 2-practicas/   # Practical exercises
│       ├── 3-recursos/    # Complementary resources
│       └── 4-asignación_dominios_aprendiz/  # Assignments
├── _docs/                 # Detailed documentation
├── scripts/               # Automation scripts
├── assets/                # Global assets (banners, etc.)
└── secrets/               # Sensitive data (gitignored)
```

---

## 🤝 Contributing

This is an educational project. Contributions are welcome! Please read our [Contributing Guidelines](./CONTRIBUTING.md) and [Code of Conduct](./CODE_OF_CONDUCT.md).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 👥 Authors & Acknowledgments

- **EPTI Development Team** - Initial work
- See [AUTHORS](./AUTHORS.md) for a complete list of contributors

---

## 📞 Support

- **Issues**: [GitHub Issues](../../issues)
- **Documentation**: [\_docs/](./_docs/)
- **Discussions**: [GitHub Discussions](../../discussions)

---

**Made with ❤️ for education and open source**
