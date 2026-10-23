# Anmay Defence — website and source-media review

This repository contains the Anmay Defence multipage site, product/engineering references, renamed media, and ten serial MOV clips showing the owner-provided reference website.

## Website

Framework-free static site, with no build step. Routes: Home; Products; About; Technology; Solutions; Clients; Projects; FAQ; Contact.

The Home page combines a radar tracking simulation with a real product trial-footage window, a sticky step-by-step system story, generation cards, a mission-package selector and a separately marked roadmap. The Products page has Gen 1 / Gen 2 selectors, a side-by-side interactive comparison table, mission-package detail and related STRIKE M / PRAHAR NETRA panels.

Shared behavior and design live in site.js and site.css, with supporting effects in site-effects.css. The visual direction uses near-black technical stages, blue scan accents, Inter Tight / Inter / JetBrains Mono, sticky scroll storytelling, scroll reveals and reduced-motion fallbacks.

## Source library audit

The inspiration_video folder holds the original ten MOV segments in their original sequence. Source Office files include three narrative/storyboard DOCX documents and the large STRIKE Gen 1/Gen 2 and PRAHAR NETRA product catalogues plus the shortlisted-media/change deck.

The workflow “Audit source documents and inspiration videos” uses sparse checkout so it does not download unrelated repository media. It extracts paragraphs/tables from DOCX; slide text, tables and speaker notes from PPTX; samples reference clips at 2 frames per second using FFmpeg; creates timestamped contact sheets; and estimates an approximate palette from sampled frames.

Once the workflow is available in the Actions tab, use “Audit source documents and inspiration videos → Run workflow”. The output is uploaded as an artifact and the review files are committed under source-review/.

## Asset cleanup and documentation

- ASSET_MAP.md contains all 223 old-to-new media path mappings.
- OLD_REPO_TREE.md records the original tree.
- NEW_REPO_TREE.md records the post-build tree.
- REPO_SUMMARY.md captures company/product information extracted from readable sources and remaining validation items.

The four paths originally configured for Git LFS have updated rules in .gitattributes. For a local clone, install Git LFS first:

    git lfs install
    git clone --branch feat/anmay-defence-multipage-site https://github.com/prathamsadavarti04-pixel/anymayDefence.git
    cd anymayDefence
    git lfs pull

## Publication checks

The product comparison reflects Gen 1 / Gen 2 descriptions and reference figures found in the supplied narrative materials. Numeric values must be checked against the current approved product specification and test conditions before procurement use. Future swarm/network/directed-energy concepts are separated from current platform descriptions. Client names and legal-registration details are not inferred from media filenames.

The contact form generates a text draft locally; it does not submit data. Connect an approved secure endpoint and verified contact channel before online lead capture.
