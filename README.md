# Imans for Grok Bot

The Imans-maintained plugin connects Grok Bot to the full
[Imans](https://imans.ai) MCP server. Query your business, work with connected
integrations, and carry out the actions your Imans connection permits.

[Português](README.pt-BR.md) · [Reviewer guide](docs/reviewer-guide.md)

## Connect

You need a Grok Bot account and an Imans account with workspace access.

1. In Grok Bot, open **Connect apps** and add Imans when its marketplace listing
   is available. Before listing, ask the Bot to add the custom MCP server
   `https://mcp.imans.ai/mcp`.
2. Complete the Imans OAuth sign-in and select your workspaces, scopes and
   connection mode in the authorization screen.
3. Ask the Bot to list your authorized Imans workspaces, then give it a task.

An existing working Imans MCP connection can continue to be used. A second
connection is unnecessary. This repository adds reusable instructions and
packaging around the same server.

The package includes an Agent Plugins 1.0 manifest (`plugin.json`) and a Cursor
plugin manifest (`.cursor-plugin/plugin.json`); both use the root `mcp.json`
and the same `skills/` directory. Import the repository with a host that
supports the relevant plugin format. Direct MCP connection and packaged skill
import are separate capabilities; this release does not claim a particular
Grok Bot local-import control exists.

## What you can do

The plugin has no client-side tool allowlist or read-only-only restriction.
It uses server discovery, so all tools exposed to your authorized connection
remain available, including future tools. Availability depends on your current
permissions, consent, modules, integrations, connection mode and server support.

Examples include sales and order lifecycle, products and services, stock and
purchasing, pricing, finance, forecasts and production, contacts, marketing,
insights, tasks/processes, workspace administration, shared memory, governed
queries, exports, private deliverables and registered live integration reads.
Supported writes include task changes, process drafts and price publication.
Discovery describes the exact supported operations and gaps for your workspace.

Try:

- “Summarize last month's Imans sales by channel and explain the metric definitions.”
- “Find this SKU, check its stock and tell me when the data was updated.”
- “Find the finance and marketing data I am allowed to query.”
- “Create a task in Imans to investigate the stock discrepancy.”
- “Prepare a process draft and show its validation findings.”
- “Preview this price publication route and show the Imans approval link.”
- “Export the full results of this governed query.”

## Permissions, actions and data

Each call uses the Imans identity that authorized the connection. Workspace
consent and current role permissions apply on every call. A read-only connection
remains read-only; installing this package does not expand an existing grant.
Authorize additional scopes through Imans when needed. Review the connected
account when using shared Bots.

Imans approvals remain authoritative. In particular, price publication requires
approval of the exact batch in Imans. Pending approval, dispatch, provider
acceptance and verification are different outcomes.

This package contains configuration and instructions. It runs no local server,
collects no credentials and adds no analytics. Requested tool results are
returned to Grok Bot through the remote Imans service. Your host's data handling
also applies. Signed file links are temporary; use returned Imans artifact links
for durable references. Widgets are optional; text and structured results work
without a supported widget renderer.

The plugin is free to install. An Imans account and applicable service access
are required. Some Imans operations can consume Usage Credits; the plugin does
not change your service plan or bypass billing controls.

## Troubleshooting and support

For an expired connection, authenticate/reconnect Imans in Connect apps. For
`permission_denied`, missing scopes or `setup_required`, follow the server's
returned reason; reconnecting does not grant a missing workspace role. Honor
rate-limit retry intervals and report partial or stale data explicitly.

Use [GitHub issues](https://github.com/imans-ai/imans-grok-plugin/issues) for
plugin defects, with secrets and business data removed. For account help, use
support inside [Imans](https://app.imans.ai). See [SECURITY.md](SECURITY.md) for
private security reports and [privacy](https://imans.ai/privacy-policy) for the
Imans policy. The platform's terms presented in Imans govern service use.

## Development

The plugin needs no Python or Node installation at runtime. From a source
checkout, maintainers can validate and package it with Python 3.11+:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s scripts -p "test_*.py"
python scripts/package.py
```

On a POSIX shell, `sh scripts/preflight.sh` runs the same checks together.

Validation checks official vendored Agent Plugins schemas, manifest consistency,
skill metadata and local references, the credential-free full MCP connection,
and package paths. Packaging validates first and writes a ZIP plus SHA-256
checksum under `dist/`, using an explicit distribution file list.

See [release and submission](docs/release.md) for publication steps. The direct
MCP connection is reported working in Grok Bot by the Imans maintainer; package
validation and in-app release acceptance are tracked separately in the reviewer
guide. Marketplace review/listing is not implied by this repository.

## License

Apache-2.0. Imans names and logos remain Imans trademarks; this license grants
no right to imply an affiliation or endorsement. See [NOTICE](NOTICE).
