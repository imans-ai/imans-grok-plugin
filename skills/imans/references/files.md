# Work with files

For a complete query export, use `start_export` with the discovered query and
an idempotency key. Follow `get_export` until the job reports its real state.
Use `cancel_export` only when cancellation is requested. Check manifest part
counts, completeness and checksums; retrieving one page or one part is not
retrieving the entire export. Request download links with `get_export_part_link`
when the user needs them, since signed links expire.

For a user-requested private deliverable, prepare the artifact, call
`create_deliverable_upload`, upload exactly the declared bytes using the
returned URL, method and headers, then call `finalize_deliverable`. Use the
declared size and checksum when present. If the host cannot perform the
required upload, report that boundary rather than claiming a saved artifact.

Retrieve an existing artifact through `get_deliverable` and
`get_deliverable_download_link`. File access remains subject to its owner and
current visibility; creating a private deliverable does not publish it.
Return the permanent Imans artifact link when supplied and distinguish it
from a short-lived signed download URL. Keep signed credentials out of logs,
public documents and source repositories.
