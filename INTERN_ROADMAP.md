# Intern Roadmap — Student Management App

Learning roadmap for onboarding an intern onto this codebase. Tasks are ordered
easy → hard and grouped into phases. Check items off as they're completed.

## Current state (for context)

Small Django 6 app: a single `student_app` with a `Student` model (name, age,
subject, marks, FK to `User`), CRUD via class-based generic views, login /
register / logout, Bootstrap templates. It works, but has real gaps in every
standard Django skill area — no tests, no `.gitignore`, no
`requirements.txt`, hardcoded secret key, no search/filter/pagination, and
minimal permission checks. That makes it a good sandbox for learning.

---

## Phase 0 — Hygiene (do first, ~half a day)

- [ ] Add `.gitignore` (`__pycache__/`, `*.pyc`, `db.sqlite3`, `.idea/`, `.venv/`)
      and `git rm --cached` the files already tracked that shouldn't be
      (`db.sqlite3`, all `__pycache__/*.pyc`).
- [ ] Add `requirements.txt` pinning the Django version.
- [ ] Move `SECRET_KEY` / `DEBUG` into environment variables (e.g.
      `python-decouple` or `django-environ`), and add a `.env.example`.

## Phase 1 — Core Django fundamentals

- [ ] Write the first real tests in `student_app/tests.py` (currently empty):
      model field validation, view permission checks (a user can't edit
      another user's student), redirect-when-not-logged-in.
- [ ] Review `StudentUpdateView` / `StudentDeleteView`'s `get_queryset`
      restriction (cross-user access currently 404s instead of returning a
      proper 403) — understand why, then improve the behavior.
- [ ] Add pagination to `StudentListView` (`paginate_by`) — the list template
      currently loops over every student with no limit.
- [ ] Add search/filter (by name/subject) using a `GET` query param — first
      hands-on use of `request.GET` inside a `ListView`.

## Phase 2 — Data modeling growth

- [ ] Extend the `Student` model: add `email`, `enrollment_date`,
      `is_active`; write and apply the migration.
- [ ] Introduce a second model, e.g. `Course` or `Grade`, related to
      `Student` via FK or M2M — first taste of relational modeling beyond one
      flat table.
- [ ] Add model-level `clean()` validation instead of relying only on field
      validators.

## Phase 3 — Forms & UX

- [ ] Replace the bare `fields = [...]` generic-view forms with an explicit
      `ModelForm` (`StudentForm`) for cleaner separation and easier custom
      validation/widgets.
- [ ] Add flash messages (`django.contrib.messages`, already installed but
      unused) on create/update/delete success.
- [ ] Clean up templates: extract repeated card/form markup into
      `{% include %}` partials; move inline `<style>` blocks into a static
      CSS file (`STATICFILES_DIRS` / `{% static %}`).

## Phase 4 — Auth & permissions

- [ ] Add role-based access — e.g. "teacher" vs "student" groups via
      Django's `Group`/`Permission` system, or a `role` field. Currently any
      authenticated user can create students and only owns what they
      personally create.
- [ ] Add the password reset flow (Django ships the views — wire up
      templates + an email backend; console backend is fine for dev).
- [ ] Decide and implement whether `StudentDetailView` / `StudentListView`
      should be public or require login (currently public) — good
      discussion point.

## Phase 5 — API & frontend (stretch)

- [ ] Add Django REST Framework; expose `Student` as a read-only API
      endpoint via serializers/viewsets.
- [ ] Optional: consume that API from a small vanilla-JS or HTMX enhancement
      (e.g. live search without a page reload) — a scoped intro to HTMX that
      pairs well with Django templates without a full SPA rewrite.

## Phase 6 — Deployment readiness (capstone)

- [ ] Split settings for dev/prod using `django-environ`; set
      `ALLOWED_HOSTS`; serve static files via `whitenoise`.
- [ ] Dockerize (`Dockerfile` + `docker-compose.yml`), swap SQLite for
      Postgres via `DATABASE_URL`.
- [ ] Add a GitHub Actions workflow running `manage.py test` + linting
      (`ruff`/`flake8`) on PRs, tying back to the tests from Phase 1.

---

## Suggested pacing

| Week | Focus |
|------|-------|
| 1 | Phase 0 – Phase 1 (hygiene + fundamentals) |
| 2–3 | Phase 2 – Phase 3 (modeling + forms) |
| 4 | Phase 4 (permissions — conceptually the trickiest so far) |
| 5+ | Phase 5 – Phase 6 (API / DevOps stretch goals) |
