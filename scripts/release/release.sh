#!/usr/bin/env bash

set -e

# get current dir
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# get current version
PACKAGE_VERSION=$(cat $DIR/../../package.json|grep version|head -1|awk -F: '{ print $2 }'|sed 's/[", ]//g')

cmd_usage="Usage: yarn release [options]

  Options:
  -t          --type                                        - release, dev or alpha
  -f          --from                                        - tag to build changelog from
  -h          --help                                        - show help
"

for i in "$@"
do
case ${i} in
    -h|--help)
        echo "$cmd_usage"
        exit 0
    ;;
    -t=*|--type=*)
      RELEASE_TYPE="${i#*=}"
    ;;
    -f=*|--from=*)
      LATEST_TAG="${i#*=}"
    ;;
esac
done

# if parameter is empty, get release type from current version
if [ -z "$RELEASE_TYPE" ]
then
 if [[ $PACKAGE_VERSION == *dev* ]]
 then
    RELEASE_TYPE="dev"
 elif [[ $PACKAGE_VERSION == *alpha* ]]
 then
    RELEASE_TYPE="alpha"
 else
    RELEASE_TYPE="release"
 fi
fi

if [[ $RELEASE_TYPE != "release" ]] && [[ $RELEASE_TYPE != "dev" ]] && [[ $RELEASE_TYPE != "alpha" ]]
then
  echo cmd_usage
  exit 1
fi

UNCOMMITTED_FILES="$(git status -su)"
if [ -n "$UNCOMMITTED_FILES" ]
then
  echo "commit or stash your changes before running this script"
  exit 1
fi

# ensure github authentication
if ! gh auth status&> /dev/null; then
  gh auth login
fi

# bump version
yarn node $DIR/bump_version.js "$RELEASE_TYPE"

NEW_PACKAGE_VERSION=$(cat $DIR/../../package.json|grep version|head -1|awk -F: '{ print $2 }'|sed 's/[", ]//g')

if [ -z "$LATEST_TAG" ]
then
  # get last tag for changelog
  LATEST_TAG=$(yarn node $DIR/find_latest_tag.js $NEW_PACKAGE_VERSION)
fi

# generate changelog
yarn node $DIR/generate_changelog.js $LATEST_TAG

echo "New version is $NEW_PACKAGE_VERSION"

VERSION_WITHOUT_PRERELEASE=${NEW_PACKAGE_VERSION%-*}
CURRENT_BRANCH=$(git branch --show-current)

if [[ $RELEASE_TYPE == "release" ]]
then
  BRANCH="master"
elif [[ $RELEASE_TYPE == "alpha" ]]
then
  BRANCH="v${VERSION_WITHOUT_PRERELEASE%.*}-alpha"
else
  BRANCH="v${VERSION_WITHOUT_PRERELEASE%.*}-dev"
fi

if [[ "$CURRENT_BRANCH" != "$BRANCH" ]]
then
 echo "you must run this script either from the master of from the dev branch"
 git checkout .
 exit 1
fi

# create branch
git checkout -b release_"$NEW_PACKAGE_VERSION"

# commit changes
git commit -am "chore(release): update changelog and version to $NEW_PACKAGE_VERSION"

# push changes
git push -u origin release_"$NEW_PACKAGE_VERSION"

# create PR
if [[ $RELEASE_TYPE == "release" ]]
then
  MILESTONE="v${VERSION_WITHOUT_PRERELEASE%.*}.x"
else
  MILESTONE="v${VERSION_WITHOUT_PRERELEASE%.*}.0"
fi

gh pr create --base $BRANCH \
             --fill \
             --title "chore(release): update changelog and bump version to $NEW_PACKAGE_VERSION" \
             --body-file $DIR/pr_description.md \
             --milestone $MILESTONE

# switch back to base branch
git checkout -
