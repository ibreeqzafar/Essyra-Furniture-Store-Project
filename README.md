<div align="center">

<img src="docs/essyra-portfolio-motion.gif" alt="Animated ESSYRA portfolio: homepage, Design Studio and ESSYRA Care screenshots float in a dimensional perspective composition" width="100%" />

<br />

<p align="center">
  <a href="https://essyra-home.vercel.app/"><img src="https://img.shields.io/badge/EXPLORE_THE_STORE-ESSYRA-30382D?style=for-the-badge" alt="Explore the ESSYRA store" /></a>
</p>

<p align="center">
  <a href="https://github.com/ibreeqzafar/dbms/actions/workflows/checks.yml"><img src="https://github.com/ibreeqzafar/dbms/actions/workflows/checks.yml/badge.svg?style=for-the-badge" alt="Website and access-control checks" /></a>&nbsp;
  <a href="https://react.dev/"><img src="https://img.shields.io/badge/React-19-30382D?style=for-the-badge&logo=react&logoColor=white" alt="React 19 documentation" /></a>&nbsp;
  <a href="https://www.typescriptlang.org/docs/"><img src="https://img.shields.io/badge/TypeScript-5-30382D?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript 5 documentation" /></a>&nbsp;
  <a href="https://supabase.com/docs"><img src="https://img.shields.io/badge/Supabase-PostgreSQL-30382D?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase and PostgreSQL documentation" /></a>&nbsp;
  <a href="https://docs.n8n.io/"><img src="https://img.shields.io/badge/n8n-Self--hosted-30382D?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n documentation" /></a>
</p>

**Considered furniture. Personal spaces.**

[Store](https://essyra-home.vercel.app/) · [Design Studio](https://essyra-home.vercel.app/studio) · [Setup](docs/guides/SETUP.md) · [Architecture](docs/guides/DESIGN-AGENT.md)

*Created by Umamah Ibreeq · Founder & CEO*

</div>

<div align="center">

<img src="docs/readme-color-divider.gif" alt="Animated raised 3D divider with color flowing along the line" width="100%" />

</div>

### A three-dimensional look at ESSYRA

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

The animated cover uses real ESSYRA screenshots in a floating, layered composition.

<div align="center">

| **01 · Explore** | **02 · Get inspired** |
|:---:|:---:|
| <img src="docs/screenshots/home-navigation.png" alt="ESSYRA homepage with room navigation and cinematic interior" width="480" /> | <img src="docs/screenshots/essyra-care.png" alt="ESSYRA Care assistant with product discovery suggestions" width="480" /> |
| Browse room collections and discover furniture. | Ask ESSYRA Care about products, orders and delivery. |

<br />

| **03 · Imagine your room** | **04 · Find your next piece** |
|:---:|:---:|
| <img src="docs/screenshots/design-studio.png" alt="ESSYRA Design Studio arranging a furniture piece in a room" width="480" /> | <img src="docs/screenshots/collection-offers.png" alt="ESSYRA furniture collection with product prices and offers" width="480" /> |
| Build a room composition in the private Design Studio. | Compare pieces, explore current offers and choose a favourite. |

</div>

<div align="center">

<img src="docs/readme-color-divider.gif" alt="Animated raised 3D divider with color flowing along the line" width="100%" />

</div>

### A home, considered from every angle

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

ESSYRA connects furniture discovery with interior inspiration. Customers browse by room, compare pieces, create a room composition and place cash-on-delivery orders. A private administration area gives the brand control over its catalogue, stock, sale prices, orders and customer care.

Built as a university DBMS project, it brings the interface, relational data model, access rules and automation workflows together in one repository.

### Explore the experience

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

| Experience | What it includes |
|---|---|
| **Furniture discovery** | Room and item categories, search, price and material filters, sorting, product details, favourites and comparison. |
| **Design Studio** | Preferences, budget and placement constraints; catalogue matching; furniture cutouts; adjustable room compositions and private saved designs. |
| **ESSYRA Care** | Shopping questions, catalogue searches, product comparisons, policy guidance and links to authenticated order/support tools. |
| **Customer accounts** | Email/password and configured Google sign-in, password recovery, owned orders and delivered-purchase reviews. |
| **Store administration** | Products, inventory, sale prices, orders, customer records and combined historical/current sales analytics: monthly comparisons, best sellers, recorded collections, optional profit planning and CSV exports. Protected by administrator permissions and MFA. |
| **Presentation** | Light/dark themes, responsive layouts, cinematic interiors, breadcrumbs, page metadata, sitemap and social previews. |

#### Agent status

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

| Component | Current implementation |
|---|---|
| **ESSYRA Care** | Local n8n workflow using Groq `openai/gpt-oss-20b` and bounded public catalogue/policy tools. |
| **Design Studio adviser** | Separate n8n workflow and conversation memory; styling guidance for the studio's matched products. |
| **Furniture placement** | Browser-based background removal, cropping and adjustable illustrative overlays. |
| **Photorealistic room editing** | Live finished-image panel, n8n/Groq room validation and FLUX editing, with a private Supabase queue and owner-only results. Pipeline/isolation tests passed and the frontend was deployed through GitHub. Generated furniture fidelity needs visual review; the laptop connector and free provider capacity must be available. [Integration notes](docs/guides/DESIGN-STUDIO-IMAGES.md). |

Self-hosted n8n Community Edition does not depend on the n8n Cloud trial. Both n8n and the connector must run on an awake, connected laptop. Groq and any image service have their own limits.

### How the pieces connect

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

<div align="center">

<img src="docs/essyra-system-flow.svg" alt="Dimensional architecture flow: storefront, Supabase authentication and database, private job queue, and laptop-hosted n8n agents" width="100%" />

</div>

The frontend is hosted on Vercel. Supabase hosts authentication, live database records, private files and backend functions. GitHub stores source code and database setup files. The laptop stores n8n's private runtime and encrypted credentials.

### Run locally

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

**Requirements:** Node.js 24, npm and a configured Supabase project for connected features.

```bash
git clone https://github.com/ibreeqzafar/dbms.git
cd dbms
npm ci
```

Copy `.env.example` to `.env.local`, then configure the public project URL, publishable key, site URL and feature flags.

```bash
npm run dev
```

Development runs at `http://127.0.0.1:4174`. Create the production build with:

```bash
npm run build
```

The build produces `dist/`, generates public SEO routes, splits large features into separate chunks and disables production source maps.

#### Start the local agents

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

For the existing configured laptop installation, double-click **Start ESSYRA Support.cmd** in the `essyra-n8n-local` setup folder. This starts n8n and the outbound website connector. Open `http://localhost:5678` to inspect workflows.

For a fresh installation from GitHub:

```bash
cd local-n8n
npm ci
npm start
```

Follow [local n8n setup](local-n8n/README.md), import the workflows in `n8n/`, select your own saved provider credentials, and configure the connector. Importing portable JSON alone does not install credentials or activate the website connection.

### Project map

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

```text
src/                    Frontend pages, components and application logic
public/                 Brand assets, interior film and original layout model
supabase/
  functions/            Backend function source and shared validation
  migrations/           Database schema, policies and incremental changes
  seed.sql              Catalogue initialization
n8n/                    Portable Care and Design Studio workflow definitions
local-n8n/              Laptop launchers, connector and dependency lockfile
scripts/                Builds, catalogue utilities and regression checks
specifications/         SRS and SDS text
.github/                Automated checks and dependency-update configuration
```

### Validate the project

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

| Command | Coverage |
|---|---|
| `npm test` | Domain rules, catalogue consistency, navigation, chat formatting and rankings. |
| `npm run test:database` | Database migrations, checkout, stock, idempotency and ownership. |
| `npm run test:admin` | Administrator MFA, role boundaries, sale prices and reporting. |
| `npm run test:studio` | Image handling, matching, private image-job permissions, leases and request limits. |
| `npm run test:support` | Chat isolation, worker leases, tickets and public ranking projections. |
| `npm run test:reviews` | Delivered-purchase reviews, privacy and invitation queues. |
| `node scripts/support-workflow-check.mjs` | Fixed read-only endpoints and portable workflow boundaries. |
| `npm run build` | Type checking, production assets and generated SEO routes. |

Database tests use disposable local PostgreSQL fixtures. Passing tests is evidence for the tested controls, not an exhaustive security guarantee. Dependencies in the local automation environment require separate review and updates.

### Deployment

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

| Vercel setting | Value |
|---|---|
| Project | `essyra-home` |
| Framework | Vite |
| Node.js | 24.x |
| Root directory | Repository root |
| Install command | `npm ci` |
| Build command | `npm run build` |
| Output directory | `dist` |

Set the public variables from `.env.example` in Vercel. To enable deployments on push, connect the repository to the existing Vercel project using the owner's GitHub Login Connection. Source upload is complete; that account-linking step was still pending at the last verified check.

Backend functions and database migrations are deployed separately. Supabase's automatic production deployment was off at the last check. Reconcile the manually installed migration history before enabling it; do not blindly rerun historical migrations against the existing database.

### Data and privacy

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

- Private customer records, room photos, credentials and n8n runtime backups do not belong in GitHub.
- Only public configuration belongs in `VITE_*` variables. Provider and service-role keys remain in secure server or n8n settings.
- Customer access is enforced by database ownership rules; staff management requires an active administrator with MFA.
- Guest recommendation access uses three successful generations with a 24-hour refill. Failed/empty matching requests do not consume a successful generation.
- Reference product media and historical project records are documented in [REFERENCE_DATA.md](docs/guides/REFERENCE_DATA.md). Confirm media rights and replace project records before real commercial use.
- COD is the current payment method. The project's delivery scheduler simulates delivery status; it does not verify a physical courier.

### Useful guides

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

[General setup](docs/guides/SETUP.md) · [Administrator guide](docs/guides/ADMIN-GUIDE.md) · [Design agent](docs/guides/DESIGN-AGENT.md) · [Support connection](docs/guides/SUPPORT-AGENT-SETUP.md) · [Customer reviews](docs/guides/CUSTOMER-REVIEWS.md) · [Furniture cutouts](docs/guides/STUDIO-EXTRACTION.md)

<div align="center">

<img src="docs/readme-color-divider.gif" alt="Animated raised 3D divider with color flowing along the line" width="100%" />

</div>

<div align="center">

#### From first inspiration to a space of your own

<img src="docs/readme-color-divider.gif" alt="" width="100%" />

<img src="docs/essyra-footer-motion.gif" alt="Animated text-only footer: an embossed ESSYRA wordmark above a moving highlight flowing through Discover, Imagine, Choose and Make It Yours" width="100%" />

<br />

**ESSYRA**

*Find the soul of your place.*

[Explore the store](https://essyra-home.vercel.app/) · [Open Design Studio](https://essyra-home.vercel.app/studio)

</div>
