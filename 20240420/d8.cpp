#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    // 各ユーザの友達リストを格納するunordered_map
    unordered_map<int, unordered_set<int>> friends;

    for (int i = 0; i < M; ++i) {
        int A, B;
        cin >> A >> B;
        A--;  // 0-indexedに調整
        B--;  // 0-indexedに調整
        friends[A].insert(B);
        friends[B].insert(A);
    }

    int new_friendships = 0;

    // 新しい友達関係をカウント
    for (int i = 0; i < N; ++i) {
        unordered_set<int> all_second_friends;

        // iの友達の友達を集める
        for (int j : friends[i]) {
            for (int k : friends[j]) {
                if (k != i && friends[i].find(k) ==
                                  friends[i].end()) {  // kはiとまだ友達ではない
                    all_second_friends.insert(k);
                }
            }
        }

        // 新しい友達関係の数をカウント
        new_friendships += all_second_friends.size();
        for (int new_friend : all_second_friends) {
            friends[i].insert(new_friend);
            friends[new_friend].insert(i);
        }
    }

    cout << new_friendships << endl;

    return 0;
}
