package a0212.pro8_전송시간;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Queue;
import java.util.TreeMap;

class Edge {
	int start, target, wei;

	public Edge(int start, int target, int wei) {
		this.start=start; this.target = target; this.wei = wei;
	}

	@Override
	public boolean equals(Object o) {
		if (this == o)
			return true;
		if (o == null || getClass() != o.getClass())
			return false;
		Edge edge = (Edge)o;
		return start == edge.start && target == edge.target;
	}

	@Override
	public int hashCode() {
		return Objects.hash(start, target);
	}
}

class Group {
	int oneToTwo, oneToThree, twoToThree; // 시작점에서 목표로 가는 총 비용
	List<Integer> target1 = new ArrayList<>(); // 1번과 연결된 다른 그룹(그룹, 비용)
	List<Integer> target2 = new ArrayList<>();
	List<Integer> target3 = new ArrayList<>();
	List<Edge> edges = new ArrayList<>(); // 연결된 간선들

	
}

class UserSolution {
	int N, K;
	int[] mNodeA, mNodeB, mTime;

	Group[] groups;
	List<Integer> root1Target = new ArrayList<>(); // 1번과 연결된 다른 그룹(그룹, 비용)
	List<Integer> root2Target = new ArrayList<>();
	List<Integer> root3Target = new ArrayList<>();
	TreeMap<Integer, HashSet<Edge>> map = new TreeMap(); // key=nodeId

	public void init(int N, int K, int mNodeA[], int mNodeB[], int mTime[]) {
		this.N = N;this.K = K;this.mNodeA = mNodeA;this.mNodeB = mNodeB;this.mTime = mTime;

		groups = new Group[N+1];
		for (int i=0; i<N+1; i++) groups[i] = new Group();

		for (int i=0; i<K; i++) {
			int groupIdA = mNodeA[i] / 100;
			int groupIdB = mNodeB[i] / 100;

			if(groupIdA == groupIdB) {
				// TODO: group 객체 안에 넣기
				groups[groupIdA].edges.add(new Edge())
			}else if(mNodeA[i] < 4 || mNodeB[i] < 4){
				// TODO: 루트에서 연결되는 groupID 저장
			}else{
				// TODO: 각자의 루트에 정보 넣기
			}
		}
	}

	public void addLine(int mNodeA, int mNodeB, int mTime) {

	}

	public void removeLine(int mNodeA, int mNodeB) {

	}

	public int checkTime(int mNodeA, int mNodeB) {
		return 0;
	}
}