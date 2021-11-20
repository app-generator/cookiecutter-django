# Change Log

## [2.0.4] 2021-09-15 
### Improvements

- Codebase update
  - `assets` & `templates` moved to `apps` folder
  - `apps/base` renamed to `apps/home`

## [2.0.3] 2021-09-14 
### Improvements & Fixes

- Patch (Minor) Bug: UI Notification Page
  - Popups were dead.
- Gulp Tooling: Minor improvement
  - `core/static/assets/gulpfile.js`

## [2.0.2] 2021-09-07
### Fixes

- Patch [#16](https://github.com/app-generator/boilerplate-code-django-dashboard/issues/16): Minor issue in Docker

## [2.0.1] 2021-09-07
### Improvements & Fixes

- Better Code formatting
- Improved Files organization
- Optimize imports
- Docker Scripts Update
- Patch 500 Error when authenticated users access `admin` path (no slash at the end)

## [2.0.0] 2021-09-01
### Improvements

- Dependencies update (all packages) 
  - Django==3.2.6 (latest stable version)

## [1.0.5] 2021-08-27
### Improvements

- Bump UI - [Volt Dashboard v1.4.1](https://github.com/themesberg/volt-bootstrap-5-dashboard/releases) 
- Added Gulp SCSS compilation scripts
  - Help can be found on README -> `Recompile CSS` section

## [1.0.4] 2021-01-04
### Bug fixing

- Read properly the `.env` variables. Impacted file(s):
    - Impacted file: **core/settings.py**

## [1.0.3] 2021-01-01
### Bug fixing, Improvements

- Routing - remove a duplicate rule
    - `admin` rule (no slash at the end)

- Auth forms
    - Login Page - update label
    - Registration - hide the form on success

- Unreported Bug - Left menu selection based on the current page. Modified files:
    - app\views.py
    - core\templates\includes\sidebar-rtl.html

- Patch #4 - Whitenoise Fix - Wrong positioning in 'core/settings.py'
    - WhiteNoiseMiddleware must be positioned right after SecurityMiddleware
    - Impacted file: **core/settings.py** / MIDDLEWARE section

## [1.0.2] 2020-06-18
### Bug fixing, Improvements

- Patch #2 - Error when access `admin` path (no trailing slash)

## [1.0.1] 2020-05-30
### Bug fixing, Improvements

- Add CHANGELOG.md to track all changes
- Patch #1 - Error-404.html not used in all contexts
- Rename error pages: error-40X become page-40X
- Update LICENSE file - added more information regarding the app usage

## [1.0.0] 2020-02-07
### Initial Release
