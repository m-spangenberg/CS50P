import emoji as e


def main():
    """The emoji movie had me :face_with_head_bandage:"""
    emo = str(input("Input: ").strip())
    print(f"Output: {e.emojize(emo, language='alias')}")


main()