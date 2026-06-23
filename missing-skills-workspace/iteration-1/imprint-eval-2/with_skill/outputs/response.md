## UI Consistency Audit

I have scanned the UI component files in this project. Here are the conflicts found across cards, buttons, and forms:

### Conflicts found

**Border radius**
- Cards: `rounded-lg`, `rounded-xl`, `rounded-2xl` (inconsistent across sessions)
- Buttons: `rounded-md`, `rounded-lg` (varies between primary and secondary)
- Forms: `rounded-md` (mostly consistent)

Recommendation: Standardize on `rounded-lg` for cards and buttons, `rounded-md` for form inputs. This matches the majority usage in newer components.

**Background colors**
- Cards: `bg-white`, `bg-gray-50`, `bg-[#f8fafc]` (hardcoded hex in older cards)
- Buttons: `bg-blue-600`, `bg-blue-500` (shade inconsistency)
- Forms: `bg-white`, `bg-gray-50` (mostly consistent)

Recommendation: Use `bg-white` for card and input surfaces, `bg-gray-50` for secondary surfaces. Replace `bg-[#f8fafc]` with `bg-gray-50`. Button primary should be `bg-blue-600` consistently.

**Text colors**
- Primary text: `text-gray-900`, `text-slate-900` (mixed Tailwind color families)
- Secondary text: `text-gray-600`, `text-slate-500` (mixed families)
- Muted text: `text-gray-400`, `text-slate-400`, `text-gray-500` (three variations)

Recommendation: Standardize on the `gray` family — `text-gray-900` primary, `text-gray-600` secondary, `text-gray-400` muted. Replace all `slate-*` variants.

**Spacing**
- Card padding: `p-4`, `p-5`, `p-6` (inconsistent internal spacing)
- Button padding: `px-4 py-2`, `px-5 py-2.5`, `px-6 py-3` (growing larger across sessions)
- Form field gaps: `gap-4`, `gap-5`, `space-y-4` (mixed utility names and values)

Recommendation: Cards use `p-6`, buttons use `px-4 py-2` (compact) or `px-5 py-2.5` (default), form fields use `space-y-4`. Do not mix `gap-*` and `space-y-*` for vertical spacing in forms.

**Border colors**
- Cards: `border-gray-200`, `border-slate-200` (mixed families)
- Buttons: `border border-gray-300` (secondary), none on primary (correct)
- Forms: `border-gray-300`, `border-gray-200` (inconsistent between default and focus states)

Recommendation: Use `border-gray-200` for card borders, `border-gray-300` for form input borders.

**Interactive states**
- Buttons: `hover:bg-blue-700`, `hover:bg-blue-500` (shade mismatch with base)
- Focus rings: `focus:ring-2 focus:ring-blue-500`, `focus:outline-none focus:ring-blue-600` (inconsistent ring width)
- Card hover: some cards have `hover:shadow-md`, others have no hover state at all

Recommendation: Button hover should be one shade darker than base (`bg-blue-600` → `hover:bg-blue-700`). Standardize focus ring to `focus:ring-2 focus:ring-blue-500 focus:ring-offset-2`. All interactive cards should have `hover:shadow-md`.

### Hardcoded values found

These bypass the design system and must be replaced with token classes:

- `bg-[#f8fafc]` — found in older card components, replace with `bg-gray-50`
- `text-[#1e293b]` — found in one card heading, replace with `text-gray-900`
- `border-[#e2e8f0]` — found in one form wrapper, replace with `border-gray-200`

### Recommended baseline

Based on the majority usage and standard Tailwind design tokens:

| Property           | Correct class     |
| ------------------ | ----------------- |
| Card background    | `bg-white`        |
| Card border        | `border-gray-200` |
| Card radius        | `rounded-lg`      |
| Card padding       | `p-6`             |
| Button primary     | `bg-blue-600`     |
| Button secondary   | `bg-white border border-gray-300` |
| Button radius      | `rounded-md`      |
| Button padding     | `px-4 py-2`       |
| Button hover       | `hover:bg-blue-700` |
| Input background   | `bg-white`        |
| Input border       | `border-gray-300` |
| Input radius       | `rounded-md`      |
| Focus ring         | `focus:ring-2 focus:ring-blue-500 focus:ring-offset-2` |
| Text primary       | `text-gray-900`   |
| Text secondary     | `text-gray-600`   |
| Text muted         | `text-gray-400`   |
| Form field spacing | `space-y-4`       |

---

Audit complete. Conflicts found across 6 properties.

Before I establish the baseline in `ui-registry.md`:
1. Do the recommendations above look correct?
2. Are there any conflicts you want to resolve differently?
3. Should I flag the hardcoded values as issues to fix?

Confirm the baseline and I will write it to `ui-registry.md`.
