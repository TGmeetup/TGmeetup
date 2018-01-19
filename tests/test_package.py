#!/usr/bin/env python3
# coding=utf-8
import json
import pytest
import subprocess
import os
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# 1. Is it a good json format? (Maybe someone let it as unformatted json file.)
# 2. Varify the json file is used 2 spaces per indent level.
# 3. Check every object


class GetFiles():
    def get_group_files(self):
        cmd = "find ~/ -name TGmeetup | sed -n '1p'"
        output = subprocess.check_output(cmd, shell=True)
        try:
            mydir = str(output.splitlines()).split("'")[1]
        except BaseException:
            mydir = str(output.splitlines())
        cmd = "du -a " + mydir + "/community " + mydir + \
            "/conference | grep package.json | awk '{print $2}'"
        output = subprocess.check_output(cmd, shell=True)
        gf_all = []
        for gf in output.splitlines():
            try:
                gf_all.append(str(gf).split("'")[1])
            except BaseException:
                gf_all.append(str(gf))
        return(gf_all)


class TestFileFormat:

    def test_isformat(self):
        message = "TEST_MESSAGE"
        try:
            get_files = GetFiles()
            all_files = get_files.get_group_files()
            for org_file in all_files:
                json.load(open(org_file))
        except pytest.raises.Exception as e:
            assert e.msg == message
        else:
            assert True, "Expected pytest.raises.Exception"

    def test_indent(self):
        get_files = GetFiles()
        all_files = get_files.get_group_files()
        for org_file in all_files:
            data = json.load(open(org_file))
            with io.open("tmplate.json", 'w', encoding='utf8') as outfile:
                str_ = json.dumps(data,
                                  indent=2, sort_keys=False,
                                  separators=(',', ': '), ensure_ascii=False)
                outfile.write(to_unicode(str_))
            f1 = open(org_file)
            f2 = open("tmplate.json")
            with f1, f2, open('outfile.txt', 'w') as outfile:
                for line1, line2 in zip(f1, f2):
                    if line2 != "}":
                        assert line1 == line2, org_file
        os.remove("tmplate.json")


class TestObjects:
    # 1. Test require fields
    # 2. Test other fields
    def test_necessary_field(self):
        get_files = GetFiles()
        all_files = get_files.get_group_files()
        for org_file in all_files:
            data = json.load(open(org_file))
            # Name
            assert isinstance(data["name"], str)
            assert len(data["name"].split()) == 1
            # Title
            assert isinstance(data["title"], str)
            # countrycode
            assert isinstance(data["countrycode"], str)
            assert len(data["countrycode"]) == 2
            # city
            assert isinstance(data["city"], str)
            # keywords
            assert isinstance(data["keywords"], list)
            # registration
            assert isinstance(data["registration"], dict)

    def test_not_necessary_field(self):
        get_files = GetFiles()
        all_files = get_files.get_group_files()
        for org_file in all_files:
            data = json.load(open(org_file))
            # description
            try:
                assert isinstance(data["description"], str)
            except BaseException:
                continue
            # homepage
            try:
                assert isinstance(data["homepage"], str)
            except BaseException:
                continue
            # contact
            try:
                assert isinstance(data["contact"], str)
            except BaseException:
                continue
            # contributors
            try:
                assert isinstance(data["contributors"], str)
            except BaseException:
                continue
            # chat
            try:
                assert isinstance(data["chat"], list)
            except BaseException:
                continue
            # social-media
            try:
                assert isinstance(data["social-media"], list)
            except BaseException:
                continue
