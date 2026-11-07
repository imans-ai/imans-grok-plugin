# Perform supported actions

Read the current operation descriptor and its availability before acting.
The user's requested change, server-side scope/role checks and connection mode
all apply. Use the operation's preview when available, preserve its payload
and revision, and execute only the requested effect.

For task creation and changes, use the matching preview and action tools.
Generate one idempotency key per intended mutation and reuse it for retries
of that same payload. Follow the returned operation ID with its status tool
after an ambiguous result. If a timeout arrives before any operation ID,
repeat the same action with the original key and identical payload to recover
its receipt, then follow its status. Creating a new key could duplicate the effect.
If the user changes the intent, preview the new intent as a new operation.

For process drafts, preserve `expected_revision`, report structural findings
and use the returned Process Studio handoff. A saved draft is distinct from
an activated process. Resolve revision conflicts from the latest server state
before preparing another edit.

For price publication, use an existing route and the Imans resolved prices.
Present the preview and the returned approval link for the exact batch.
Approval required by Imans is completed in Imans. A Grok Bot approval card or
a user saying “approved” in chat does not replace that recorded approval.
Follow the publication receipt: dispatch, provider acceptance and readback
verification are separate states. An uncertain result is reconciled through
its status operation; do not resend the batch to resolve uncertainty.

For other supported actions, follow the live descriptor's preview, approval,
idempotency, verification and recovery contract. New server operations remain
eligible without editing this skill when the authenticated connection permits
them. Discovery entries marked unsupported are not executable promises.

Return operation ID, actual state, relevant Imans link, and any next step.
Use “pending approval”, “in progress”, “partial”, or “uncertain” when those are
the returned states. Confirm completion only from the operation's outcome.
