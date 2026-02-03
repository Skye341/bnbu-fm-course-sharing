######################################
# 文档更新脚本
#
# author: Jinsui Liu
# email: 3125124390@qq.com
# date: 2026/02/03
#
######################################

from pathlib import Path
import yaml
from typing import List, Dict


def readme_process():
    """
    Find all the readme file in course folders,
    then copy them to docs with adding file tree.
    """

    def readme_gen(readme_path: Path, folder: Path):
        """
        Copy readme files from course folders to docs path,
        and generate the file tree of course folders.
        """
        try:
            # 读取现有内容
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 生成递归的文件列表部分
            file_list_section: str = generate_recursive_file_list(
                folder, base_path=folder
            )

            # 替换或添加文件列表部分
            if content.endswith("\n"):
                new_content = content + file_list_section
            else:
                new_content = content + "\n" + file_list_section

            # 获取课程名称
            courseName = folder.relative_to(folder.parent)

            # 写入更新后的内容
            DashedName = str(courseName).replace(" ", "-")
            docs_path = folder.parent / "docs" / (DashedName + ".md")
            with open(docs_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"已更新: {docs_path}")
        except Exception as e:
            print(f"处理 {readme_path} 时出错: {e}")

    def generate_recursive_file_list(
        folder: Path, base_path: Path, indent_level=0
    ) -> str:
        items: List[str] = []
        for item in sorted(
            folder.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())
        ):
            if item.name.lower() == "readme.md":
                continue
            if item.name.lower().startswith("."):
                continue

            relatedDIR = (
                str(item.relative_to(current_dir))
                .replace(" ", "%20")
                .replace("\\", "/")
            )
            indent = "".join(["&nbsp"] * 4 * indent_level)
            if item.is_dir():
                items.append("<details>")
                items.append(
                    f'<summary><a href="https://github.com/FM-Course/bnbu-fm-course-sharing/blob/master/{relatedDIR}/">{indent}📁 {item.name}</a></summary>'
                )
                items.append(
                    generate_recursive_file_list(item, base_path, indent_level + 1)
                )
                items.append("</details>")
            else:
                items.append(
                    f'{indent} • <a href="https://github.com/FM-Course/bnbu-fm-course-sharing/blob/master/{relatedDIR}">📄 {item.name}</a><br>'
                )

        if indent_level == 0 and not items:
            items.append("- (空文件夹)")

        result = "\n".join(items)
        if indent_level == 0:
            return "## 文件列表\n" + result + "\n"
        else:
            return result

    current_dir = Path(__file__).parent

    for subdir in current_dir.glob("*"):
        if str(subdir.relative_to(current_dir)) == "docs":
            continue

        if subdir.is_dir():
            readme_path = subdir / "readme.md"

            # 检查是否存在readme.md文件（不区分大小写）
            if readme_path.exists():
                readme_gen(readme_path, subdir)


def generate_mkdocs():
    def parse_rank(rank_str):
        rank_str = rank_str.strip()
        if "." in rank_str:
            parts = rank_str.split(".")
            if len(parts) == 3:
                return (int(parts[0]), int(parts[1]), int(parts[2]))
        rank_int = int(rank_str)
        rank_padded = f"{rank_int:03d}"
        return (int(rank_padded[0]), int(rank_padded[1]), int(rank_padded[2]))

    def rank_to_version(rank_str):
        rank_str = rank_str.strip()
        if "." in rank_str:
            return rank_str
        rank_int = int(rank_str)
        rank_padded = f"{rank_int:03d}"
        return f"{rank_padded[0]}.{rank_padded[1]}.{rank_padded[2]}"

    course_info = []
    for item in Path(__file__).parent.iterdir():
        if (
            item.is_dir()
            and item.name.lower() != ".git"
            and item.name.lower() != "docs"
        ):
            readme_path = item / "README.md"
        else:
            continue

        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"读取 {readme_path} 失败: {e}")
            continue

        if content.startswith("---"):
            yaml_end = content.find("---", 3)
            if yaml_end != -1:
                yaml_content: str = content[3:yaml_end].strip()
                metadata: Dict = yaml.safe_load(yaml_content)
                title: str = metadata.get("title", "")
                code: str = metadata.get("code", "")
                category: str = metadata.get("category", "")
                rank_raw: str = str(metadata.get("rank", ""))
        else:
            raise ValueError(f"{readme_path} 缺少 YAML 头信息")

        rank_parsed = parse_rank(rank_raw)
        rank_version = rank_to_version(rank_raw)

        course_info.append(
            {
                "title": title,
                "code": code,
                "category": category,
                "rank_tuple": rank_parsed,
                "rank": rank_version,
            }
        )

    course_info = sorted(course_info, key=lambda x: x["rank_tuple"])

    category_titles = {
        "MR": "Major Require",
        "ME": "Major Elective",
        "FE": "Free Elective",
        "GE": "General Education",
        "UC": "University Core",
        "Other": "Other Materials",
    }

    list_str = "# 收录课程名录\n|Course Title|Course Code|Category|\n|-|-|-|\n"
    list_str += "\n".join(
        f"|{course['title']}|{course['code']}|{course['category']}|"
        for course in course_info
    )
    with open(Path(__file__).parent / "docs" / "list.md", "w", encoding="utf-8") as f:
        f.write(list_str)

    mkdocsContent = (
        "site_name: BNBU-FM课程攻略\n"
        "theme: readthedocs\n"
        "repo_url: https://github.com/FM-Course/bnbu-fm-course-sharing\n"
        "\n"
        "nav:\n"
        "  - 首页: index.md\n"
        "  - 食用方法: usage.md\n"
        "  - 贡献: contribute.md\n"
        "  - 收录课程名录: list.md\n"
        "  - 致谢: thanks.md\n"
    )

    for cat_code in ["MR", "ME", "FE", "GE", "UC", "Other"]:
        cat_courses = [c for c in course_info if c["category"] == cat_code]
        if cat_courses:
            mkdocsContent += f"  - {category_titles[cat_code]}:\n"
            for course in cat_courses:
                mkdocsContent += (
                    f"    - {course['title']}: {course['title'].replace(' ', '-')}.md\n"
                )

    with open(Path(__file__).parent / "mkdocs.yml", "w", encoding="utf-8") as f:
        f.write(mkdocsContent)


if __name__ == "__main__":
    readme_process()
    generate_mkdocs()
