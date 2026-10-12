# DMC Lite Shield Documentation

This repository contains the public customer-facing documentation for the **DMC Lite Shield** – an Arduino Giga R1 motion control shield for Dragonframe stop-motion software.

**Product website**: [www.dmclite.com](https://www.dmclite.com)

**Documentation site**: [dmclite.github.io/dmc-lite-shield-docs](https://dmclite.github.io/dmc-lite-shield-docs) (once GitHub Pages is enabled)

## About This Repository

This documentation repository contains:

- Customer manual and setup guides
- Hardware specifications and wiring information
- Firmware installation instructions
- Dragonframe configuration guides
- Troubleshooting and FAQ

**Note**: This is the PUBLIC documentation repository only. Hardware design files, firmware source code, BOM, and internal pricing information are maintained in a separate private repository.

## Documentation Structure

The documentation is built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

```
docs/
├── index.md                    # Home page
├── getting-started/
│   ├── overview.md            # Product overview
│   ├── whats-in-the-box.md   # Package contents
│   └── prerequisites.md       # Required components
├── hardware/
│   ├── specifications.md      # Technical specifications
│   └── wiring.md             # Wiring and connections
├── setup/
│   ├── firmware.md           # Firmware installation
│   ├── dragonframe.md        # Dragonframe configuration
│   └── estop.md              # E-stop setup
├── troubleshooting.md         # Common issues and solutions
├── faq.md                     # Frequently asked questions
└── support.md                 # Support and contact
```

## Editing the Documentation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Local Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/dmclite/dmc-lite-shield-docs.git
   cd dmc-lite-shield-docs
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Previewing Changes Locally

To preview the documentation site locally:

```bash
mkdocs serve
```

This will start a local development server at `http://127.0.0.1:8000`. The site will automatically reload when you save changes to the documentation files.

### Editing Content

1. Documentation pages are written in Markdown and located in the `docs/` directory
2. Edit existing `.md` files or create new ones
3. Update `mkdocs.yml` if you add, remove, or rename pages
4. Preview your changes with `mkdocs serve`
5. Commit and push when satisfied

### Building the Site

To build the static site (not usually necessary as GitHub Actions handles this):

```bash
mkdocs build
```

This creates a `site/` directory with the generated HTML.

## Deployment

The documentation is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the `main` branch.

### Enabling GitHub Pages (First-Time Setup)

After this pull request is merged, a repository administrator needs to enable GitHub Pages:

1. Go to repository **Settings** > **Pages**
2. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
3. The site will be available at: `https://dmclite.github.io/dmc-lite-shield-docs/`

The GitHub Actions workflow (`.github/workflows/deploy-docs.yml`) will automatically build and deploy the site on every push to `main`.

## TODO Items

Several sections in the documentation are marked with TODO placeholders where information was not available on the dmclite.com website. These sections need to be completed with accurate information:

### High Priority TODOs

1. **What's in the Box**: List of items included with the shield
2. **Pinouts**: RJ45, DB37, and 2.5mm jack pinouts and wiring diagrams
3. **Firmware Installation**: Exact paths and step-by-step instructions from README.rtf
4. **Dragonframe Configuration**: Detailed setup steps and channel configuration
5. **Camera Control**: Compatible cameras, wiring, and setup instructions
6. **E-Stop Wiring**: Connector details and connection instructions

### Medium Priority TODOs

1. **Hardware Specifications**: Physical dimensions, electrical specs, environmental specs
2. **Prerequisites**: Specific driver/motor recommendations and compatibility info
3. **Version Requirements**: Minimum Dragonframe version and compatibility notes
4. **Warranty & Returns**: Warranty terms and return policy

### Low Priority TODOs

1. **Support Contact**: Email, phone, and support hours
2. **Community Resources**: Forums, social media, user groups
3. **Cable Specifications**: Maximum lengths, shielding requirements

See individual documentation pages for detailed TODO markers.

## Contributing

When adding or updating documentation:

1. Ensure all factual claims are accurate and based on verified sources
2. Use clear, concise language appropriate for customer-facing documentation
3. Add TODO markers for any information you cannot verify
4. Test your changes locally with `mkdocs serve` before committing
5. Follow the existing documentation structure and style

## License

The documentation content in this repository is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE) (CC BY 4.0).

The DMC Lite Shield hardware and firmware are proprietary and not included in this repository.

## Support

For questions about the DMC Lite Shield:

- Visit [www.dmclite.com](https://www.dmclite.com)
- See the [Support page](docs/support.md) in the documentation

For issues with this documentation repository:

- Open an issue on GitHub
- Submit a pull request with corrections or improvements
