from providers.github import GithubReleaseProvider
from utils.comparator import compare
from storage.json_storage import load_state, save_state


provider = GithubReleaseProvider("pallets/flask")


old_state = load_state()

new_state = provider.get_state()


changes = compare(
    old_state,
    new_state
)


print("Changes:")
print(changes)


save_state(new_state)